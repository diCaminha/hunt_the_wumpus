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
		borders.append(str(i))

## Cookie stuff ##
cookie['Graph'] = graph
cookie['Arrows'] = number_arrows
cookie['Borders'] = borders
cookie['Wumpus'] = wumpus
cookie['Bats'] = bats
cookie['Pits'] = pits
cookie['Room'] = curently_room
cookie['Option'] = 1

print(cookie)
print('Content-Type: text/html')
print()
print('<html><body>')

print("You are in room # ", cookie['Room'].value)
print("You can move to rooms ", cookie['Borders'].value)

print('''<form method='get' action='/cgi-bin/htw-web.py'>
      <input class='form-control no-border-radius' type='text' name='option' placeholder='Enter m or s'/>
      <input class='form-control no-border-radius' type='text' name='room' placeholder='Enter room number(s)'/>
	    <input class='btn btn-default no-border-radius' style='margin-top: 5px;' type='submit' value='Submit' />
		  </form>''')

print("</body></html>")
