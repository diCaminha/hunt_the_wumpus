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
room = int(cookie['Room'].value)


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
<link href='../includes/Bootstrap/css/bootstrap.min.css' rel='stylesheet' type='text/css'>
<script type='text/javascript' src='includes/Bootstrap/js/bootstrap.min.js'></script>''')

# Retrieve cookie values and save them in variables
option = cookie['Option'].value	
wumpus = int(cookie['Wumpus'].value)
bats = int(cookie['Bats'].value)
pits = int(cookie['Pits'].value)
arrows = cookie['Arrows'].value
option = cookie['Option'].value
gameOver = cookie['GameOver'].value

# Check if game has already ended. If so redirect them to start game over
if (gameOver == '1'):
	print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>Sorry, you lost. :(</h2>")
	print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")

# Check if player is in same room as Wumpus	
elif (room == wumpus):
	cookie['GameOver'] = 1
	print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You ended up in the same room as the Wumpus. Game Over!</h2>")
	print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")

# Check if player is in the same room as the Pits	
elif (room == pits):
	cookie['GameOver'] = 1
	print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You fell into a pit. Game Over!</h2>")
	print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")

# Check if player is in the same room as the bats
elif (room == bats):
	room = random.choice(random_sequency_caves)
	
	# if new room is same as wumpus then end the game
	if (room == wumpus):
		print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You landed in a room with bats and they flew you to the Wumpus. :( Game over.</h2>")
		print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")
	# if new room is same as pit then end the game
	elif (room == pits):
		print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You landed in a room with bats and they flew you into a pit. :( Game over.</h2>")
		print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")
	# if new room is not wumpus or pits then redirect them to it
	else:
		cookie['Room'] = room
		print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You landed in a room with bats. They've moved you to a new room!</h2>")
		print("<a href='htw-web.py?option=m&room={0}' class='btn btn-default' role='button'>Click to Continue</a></div>".format(room))
		print(cookie)



	

# Player is in empty room, continue game	
else:
	# Display current player status #
	print("""<div class='container text-center'><div class='jumbotron'>
	<h2 style='color: red'>Player Status:</h2>
	<p>You are in room # """, room, "<br />")	
	print("You can move to rooms ", borders, "<br />")
	print("You have ", arrows, " arrow(s) left</p></div></div>")
	
	print("<div class='container text-center' style='border: 1px solid #fff'>")
	# Check and display if Wumpus, Bats, or Pits are nearby #
	if int(wumpus) in borders:
		print("<h2 style='color: red'>Careful!</h2>")
		print("<h4 style='margin-top: 0'>I smell a wumpus!</h4>")
	if int(bats) in borders:
		print("<h2 style='color: red'>Careful!</h2>")
		print("<h4 style='margin-top: 0'>Bats nearby!</h4>")
	if int(pits) in borders:
		print("<h2 style='color: red'>Careful!</h2>")
		print("<h4>I feel a draft!</h4>")
		
	# Display form with with option of move/shoot and what rooms they can travel to
	print("<br /><form method='get' action='/cgi-bin/htw-web.py'>")
	print("Choose an option: ")
	print("<select name='option' style='color: #404040'>")
	print("<option value='m'>Move</option>")
	print("<option value='s'>Shoot</option>")
	print("</select><br /><br />")
	print("Pick a room: ")
	print("<select name='room' style='color: #404040'>")
	# Only put rooms that they are allowed to travel to in the dropdown
	for i in range (0,3):
		print("<option value='{0}'>{1}</option>".format(borders[i], borders[i]))
	print("</select><br /><br /><input class='btn btn-default' style='margin-top: 5px;' type='submit' value='Submit' /></form></div>")




print('</body></html>')
