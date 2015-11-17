import random


# Creates a list containing 20 lists initialized to 0
graph = [[0 for x in range(21)] for x in range(21)] 


all_caves = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random_sequency_caves = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
copy_random_sequency_caves = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(1,21):
	cave = random.choice(all_caves)
	all_caves.remove(cave)
	random_sequency_caves[i] = cave
	copy_random_sequency_caves[i] = cave

#removing the number 0 extra in both tuple
random_sequency_caves.remove(0)
copy_random_sequency_caves.remove(0)

#Choosing the bats, pits and wumpus
bats = random.choice(random_sequency_caves)
random_sequency_caves.remove(bats)
pits = random.choice(random_sequency_caves)
random_sequency_caves.remove(pits)
wumpus = random.choice(random_sequency_caves)


#Those represents the layers of the graph, 
#which is formed by 5 caves in the first layer, 10 in the second, and finally 5 caves in the third
layer1 = []
layer2 = []
layer3 = []


########### CHOOSING RANDOMLY THE CAVES FOR EACH LAYER  #################

##choosing the caves for the first layer
for i in range(5):
	cave = random.choice(copy_random_sequency_caves)
	layer1.append(cave)
	copy_random_sequency_caves.remove(cave)

##choosing the caves for the second layer
for i in range(10):
	cave = random.choice(copy_random_sequency_caves)
	layer2.append(cave)
	copy_random_sequency_caves.remove(cave)

##choosing the caves for the third layer
for i in range(5):
	cave = random.choice(copy_random_sequency_caves)
	layer3.append(cave)
	copy_random_sequency_caves.remove(cave)



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
borders = []

option = int(input("enter the number of the option you want\n"
		+"1. choose a room to go\n"
		+"2. guess where's the wumpus\n"))
if option == 1:
	curently_room = int(input("choose a room: "))
	print("you are in ",curently_room)
	
	for i in range(1,21):
		if(graph[curently_room][i] == 1):
			borders.append(i)	
		
	print("you can move to: ")
	print(borders)

while not game_over:
	option = int(input("enter the number of the option you want\n"
		+"1. choose a room to go\n"
		+"2. guess where's the wumpus\n"))
	if option == 1:
		
		curently_room = int(input("choose a room: "))
		while(curently_room not in borders):
			print("you must to choose a room among",borders)
			curently_room = int(input("choose a room: "))

		if curently_room == wumpus:
			print("you're in the wumpus! GAME OVER!!!")
			game_over = True	
		elif curently_room == bats:
			print("you're in the bats! GAME OVER!!!")
			game_over = True
		elif curently_room == wumpus:
			print("you're in the pits! GAME OVER!!!")
			game_over = True
		
		else:	 

			print("you are in ",curently_room)
			
			borders = []	
			for i in range(1,21):
				if(graph[curently_room][i] == 1):
					borders.append(i)	
			
	########Checking if there's a wumpus,bats or pits nearby the current cave
			if wumpus in borders:
				print("I smell a wumpus!")
			if bats in borders:
				print("Bats nearby!")
			if pits in borders:
				print("I fell a draft!")
			
	#########################################################
			
			print("you can move to:",borders)
			print()
			

