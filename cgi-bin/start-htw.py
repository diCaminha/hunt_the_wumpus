#!/usr/bin/env python3
import http.cookies
import cgi
import cgitb
import functions
import os

cgitb.enable()

cookie = http.cookies.SimpleCookie()


# Creates a list containing 20 lists initialized to 0
graph = [[0 for x in range(21)] for x in range(21)] 


#call function to create the random sequency of caves
random_sequency_caves = functions.create_randomSequency_caves()


#Those represents the layers of the graph, 
#which is formed by 5 caves in the first layer, 10 in the second, and finally 5 caves in the third
layer1 = []
layer2 = []
layer3 = []


########### CHOOSING THE CAVES FOR EACH LAYER  #################

##slicing the main list random_sequency_caves, for each layer
layer1 = random_sequency_caves[0:5]
layer2 = random_sequency_caves[5:15]
layer3 = random_sequency_caves[15:20]



############ FILLING THE GRAPH #########################

graph[layer1[0]][layer1[-1]] = 1
graph[layer1[-1]][layer1[0]] = 1

for i in range(4):
	graph[layer1[i]][layer1[i+1]] = 1
	graph[layer1[i+1]][layer1[i]] = 1

graph[layer2[0]][layer2[-1]] = 1
graph[layer2[-1]][layer2[1]] = 1

for i in range(9):
	graph[layer2[i]][layer2[i+1]] = 1
	graph[layer2[i+1]][layer2[i]] = 1
	
graph[layer3[0]][layer3[-1]] = 1
graph[layer3[-1]][layer3[1]] = 1

for i in range(4):
	graph[layer3[i]][layer3[i+1]] = 1
	graph[layer3[i+1]][layer3[i]] = 1


#connections between layers 1,2 and 3
for i in range(5):

	graph[layer1[i]][layer2[2*i]] = 1
	graph[layer2[2*i]][layer1[i]] = 1
	
	graph[layer2[(i*2)+1]][layer3[i]] = 1
	graph[layer3[i]][layer2[(i*2)+1]] = 1

########### END FILLING THE GRAPH #########


game_over = False
number_arrows = 5
borders = []
form = cgi.FieldStorage()

startRoom = form.getvalue("startroom")
curently_room = int(startRoom)


#Getting caves to wumpus, pits and bats
wumpus = functions.get_cave_for_wumpus(curently_room)
bats = functions.get_cave_for_bats(curently_room,wumpus)
pits = functions.get_cave_for_pits(curently_room,wumpus,bats)

#print(wumpus,bats,pits)

for i in range(1,21):
	if(graph[curently_room][i] == 1):
		borders.append(i)

## Cookie stuff ##
cookie['Graph'] = graph
cookie['Arrows'] = number_arrows
cookie['Borders'] = borders
cookie['Wumpus'] = wumpus
cookie['Bats'] = bats
cookie['Pits'] = pits
cookie['Room'] = curently_room
cookie['Option'] = 1
cookie['GameOver'] = 0

print(cookie)
print('Content-Type: text/html')
print()
print('<html><body>')

# HTML styles and stuff
print('''<head><title>Hunt the Wumpus!</title></head>
<link href='../includes/style.css' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=PT+Sans:400,700' rel='stylesheet' type='text/css'>
<link href='../includes/Bootstrap/css/bootstrap.min.css' rel='stylesheet' type='text/css'>
<script type='text/javascript' src='includes/Bootstrap/js/bootstrap.min.js'></script>''')


if (cookie['GameOver'].value == '1'):
	print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>Sorry, you lost. :(</h2>")
	print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")
else:
	
	if (curently_room == wumpus):
		cookie['GameOver'] = 1
		print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You ended up in the same room as the Wumpus. Game Over!</h2>")
		print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")

	# Check if player is in the same room as the Pits	
	elif (curently_room == pits):
		cookie['GameOver'] = 1
		print("<div class='container text-center' style='margin-top: 25px; color: red;'><h2>You fell into a pit. Game Over!</h2>")
		print("<a href='../start.html' class='btn btn-default' role='button'>Start Over!</a></div>")

	# Check if player is in the same room as the bats
	elif (curently_room == bats):
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
			
	#Player is in empty room, continue game
	# Display current player status #
	print("""<div class='container text-center'><div class='jumbotron'>
	<h2 style='color: red'>Player Status:</h2>
	<p>You are in room # """, curently_room, "<br />")	
	print("You can move to rooms ", borders, "<br />")
	print("You have ", number_arrows, " arrow(s) left</p></div></div>")
	
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

print("</body></html>")
