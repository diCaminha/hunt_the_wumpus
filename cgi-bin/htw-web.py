#!/usr/bin/env python3

import http.cookies
import cgi
import cgitb
import functions
import os
import random


cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string == '':
    output = "I don't see a cookie."
else:
    cookie = http.cookies.SimpleCookie()
    cookie.load(cookie_string)
    
cgitb.enable()

random_sequency_caves = functions.create_randomSequency_caves()

form = cgi.FieldStorage()
form2 = cgi.FieldStorage()
formRoom = form.getvalue("room")
formOption = form2.getvalue("option")
cookie['Room'] =  formRoom
cookie['Option'] = formOption
room = cookie['Room'].value


graph = eval(cookie['Graph'].value)
	
borders = []	
for i in range (1,21):
	if(graph[int(room)][i] == 1):
		borders.append(i)

		

print('Content-Type: text/html')
print(cookie)
print()
print('<html><body>')

# HTML styles and stuff
print('''<head><title>Hunt the Wumpus!</title></head>
<link href='../includes/style.css' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=PT+Sans:400,700' rel='stylesheet' type='text/css'>
<link href='includes/Bootstrap/css/bootstrap.min.css' rel='stylesheet' type='text/css'>
<script type='text/javascript' src='includes/Bootstrap/js/bootstrap.min.js'></script>''')

option = cookie['Option'].value	
wumpus = int(cookie['Wumpus'].value)
bats = int(cookie['Bats'].value)
pits = int(cookie['Pits'].value)
arrows = cookie['Arrows'].value
option = cookie['Option'].value
gameOver = cookie['GameOver'].value
	
print("<p>Wumpus: ", wumpus, "<br />Pits: ", pits, "<br />Bats: ", bats, "</p>")

# Check if game has already ended. If so redirect them to start game over
if (gameOver == '1'):
	print("<p>Sorry, you lost. :(</p>")
	print("<a href='../start.html'>Click here to start over</a>")

# Check if player is in same room as Wumpus	
elif (room == wumpus):
	cookie['GameOver'] = 1
	print("<p>You ended up in the same room as the Wumpus. Game Over!</p>")
	print("<a href='../start.html'>Click here to start over</a>")

# Check if player is in the same room as the Pits	
elif (room == pits):
	cookie['GameOver'] = 1
	print("You fell into a pit. Game Over!")
	print("<a href='../start.html'>Click here to start over</a>")

# Check if player is in the same room as the bats
elif (int(room) == bats):
	room = random.choice(random_sequency_caves)
	
	if (room == wumpus):
		print("<p>You landed in a room with bats and they flew you to the Wumpus. :( Game over.</p>")
		print("<a href='../start.html'>Click here to start over</a>")
	elif (room == pits):
		print("<p>You landed in a room with bats and they flew you into a pit. :( Game over.</p>")
		print("<a href='../start.html'>Click here to start over</a>")
	else:
		cookie['Room'] = room
		print("You landed in a room with bats. They've moved you to a new room!")
		print("<a href='htw-web.py?option=m&room={0}'>Click here to continue</a>".format(room))
		print(cookie)



	

# Player is in empty room, continue game	
else:
	# Display current player status #
	print("<p>You are in room # ", room, "</p>")	
	print("<p>You can move to rooms ", borders, "</p>")
	print("<p>You have ", arrows, " arrow(s) left</p>")

	# Check and display if Wumpus, Bats, or Pits are nearby #
	if int(wumpus) in borders:
		print("<p>I smell a wumpus!</p>")
	if int(bats) in borders:
		print("<p>Bats nearby!</p>")
	if int(pits) in borders:
		print("<p>I feel a draft!</p>")
		
	print("<form method='get' action='/cgi-bin/htw-web.py'>")
	print("Choose an option: ")
	print("<select name='option'>")
	print("<option value='m'>Move</option>")
	print("<option value='s'>Shoot</option>")
	print("</select><br />")
	print("Pick a room: ")
	print("<select name='room'>")
	for i in range (0,3):
		print("<option value='{0}'>{1}</option>".format(borders[i], borders[i]))
	print("</select><br /><input class='btn btn-default no-border-radius' style='margin-top: 5px;' type='submit' value='Submit' /></form>")




print('</body></html>')
