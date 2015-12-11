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

form = cgi.FieldStorage()
formRoom = form.getvalue("room")	

cookie['Room'] = formRoom

print('Content-Type: text/html')
print(cookie)
print()
print('<html><body>')

room = cookie['Room'].value
graph = cookie['Graph'].value
newGraph = eval(graph)
borders = cookie['Borders'].value
borders = []	
for i in range (1,21):
	if(newGraph[int(room)][i] == 1):
		borders.append(str(i))
wumpus = cookie['Wumpus'].value
bats = cookie['Bats'].value
pits = cookie['Pits'].value
arrows = cookie['Arrows'].value
option = cookie['Option'].value
gameOver = cookie['GameOver'].value

print("<p>Wumpus: ", wumpus, "<br />Pits: ", pits, "<br />Bats: ", bats, "</p>")
# Check if game has already ended. If so redirect them to start game over
if (cookie['GameOver'].value == 1):
	print("<p>Sorry, you lost. :(</p>")
	print("<a href='../start.html'>Click here to start over</a>")

# Check if player is in same room as Wumpus	
elif (room == wumpus):
	cookie['GameOver'] = 1
	print("<p>You ended up in the same room as the Wumpus. Game Over!</p>")
	print("<a href='../start.html'>Click here to start over</a>")

# Check if player is in the same room as the Pits	
elif (str(room) in str(pits)):
	print("You fell into a pit. Game Over!")
#elif (str(room) in str(bats)):
	#print("You're in a room with bats. They've moved you to a new room!")
	#room = random.choice(start-htw.random_sequency_caves)
	#if (room == wumpus or str(room) in str(pits)):
		#print("Oops...you died. Game Over!")
	#else:
		#cookie['Room'] = room

# Player is in empty room, continue game	
else:
	# Display current player status #
	print("<p>You are in room # ", room, "</p>")	
	print("<p>You can move to rooms ", borders, "</p>")

	# Check and display if Wumpus, Bats, or Pits are nearby #
	if str(wumpus) in borders:
		print("<p>I smell a wumpus!</p>")
	if str(bats) in borders:
		print("<p>Bats nearby!</p>")
	if str(pits) in borders:
		print("<p>I feel a draft!</p>")
		
	print('''<form method='get' action='/cgi-bin/htw-web.py'>
    <input class='form-control no-border-radius' type='text' name='option' placeholder='Enter m or s'/>
    <input class='form-control no-border-radius' type='text' name='room' placeholder='Enter room number(s)'/>
    <input class='btn btn-default no-border-radius' style='margin-top: 5px;' type='submit' value='Submit' />
	  </form>''')




print('</body></html>')
