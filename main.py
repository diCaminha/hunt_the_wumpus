import random


# Creates a list containing 20 lists initialized to 0
graph = [[0 for x in range(21)] for x in range(21)] 

all_caves = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random_sequency_caves = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
wumpus = 0
bats = 0
pits = 0

#Function to generate a randomly sequence of caves 
def create_randomSequency_caves():
	for i in range(1,21):
		cave = random.choice(all_caves)
		all_caves.remove(cave)
		random_sequency_caves[i] = cave
	random_sequency_caves.remove(0)

#choose a cave for the wumpus
#it should be different from the start cave
def get_cave_for_wumpus(start_cave):
	done = False
	while not done:
		wumpus = random.choice(random_sequency_caves)
		if wumpus != start_cave:
			done = True
	return wumpus

#choose a cave for the bats
# it should be different from the first chosen cave and from where the wumpus is
def get_cave_for_bats(start_cave,wumpus_cave):
	done = False
	while not done:
		bats = random.choice(random_sequency_caves)
		if bats != start_cave and bats != wumpus_cave:
			done = True
	return bats

#choose a cave for the bats
# it should be different from the first chosen cave, also cannot be where the wumpus and the bats are!
def get_cave_for_pits(start_cave,wumpus_cave,bats_cave):
	done = False
	while not done:
		pits = random.choice(random_sequency_caves)
		if pits != start_cave and pits != wumpus_cave and pits!=bats_cave:
			done = True
	return pits



#call function to create the random sequency of caves
create_randomSequency_caves()


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

#GAME BEGINING - first choice of cave to start
curently_room = int(input("choose a cave to start: "))
print("you are in:",curently_room)

#Getting caves to wumpus, pits and bats
wumpus = get_cave_for_wumpus(curently_room)
bats = get_cave_for_bats(curently_room,wumpus)
pits = get_cave_for_pits(curently_room,wumpus,bats)

print(wumpus,bats,pits)

for i in range(1,21):
	if(graph[curently_room][i] == 1):
		borders.append(i)	

print("you can move to: ")
print(borders)

## MAIN LOOP
# the game will be running until the player guess where is the wumpus or 
# if it's game over: come in a cave where the bats, pits or wumpus are.
while not game_over:
	option = int(input("enter the number of the option you want\n"
		+"1. choose a room to go\n"
		+"2. shoot where's the wumpus\n"))
	if option == 1:
		
		
		for i in range(1,21):
			if(graph[curently_room][i] == 1):
				borders.append(i)
		
		curently_room = int(input("choose a cave to go: "))
		while(curently_room not in borders):
			print("you must to choose a room among",borders)
			curently_room = int(input("choose a room: "))

		if curently_room == wumpus:
			print("you're in the wumpus! GAME OVER!!!")
			game_over = True	
		elif curently_room == bats:
			print("you're in the bats! GAME OVER!!!")
			game_over = True
		elif curently_room == pits:
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
	
	## Shooting in the wumpus		
	elif option == 2:
		#cleaning the borders	
		borders = []	
		for i in range(1,21):
			if(graph[curently_room][i] == 1):
				borders.append(i)
		
		path = [curently_room]
		previous_cave = curently_room

		print("\nYou can create a path with 1-5 caves to kill the wumpus.")
		done = False
		while not done:
			
			cave = int(input("Enter the next cave of the path:"))
			if cave in path:
				print(" this cave is already in your path! Try another cave.")
			elif cave not in borders:
				print("this cave is not connected to the previous cave! Try another cave.")
			else:
				
				path.append(cave)
				
				borders = []	
				for i in range(1,21):
					if(graph[cave][i] == 1):
						borders.append(i)
				print("your path is:",path)
				opt = int(input("choose what you want:\n1.SHOOT!\n2.add another cave"))
				if opt == 1:
					done = True
		print(path)		
		##After shooting the arrow through the path
		if path[-1] == wumpus:
			print("YOU KILL THE WUMPUS!! YOU WIN!!")
			game_over = True
		else:
			number_arrows -= 1
			if(number_arrows < 1):
				print("You don't have arrows anymore!!")
				break
			print("you miss the WUMPUS.\nNow you have ",number_arrows,"lefting!!")
			#realocating the wumpus
			isRealocated = False
			while not isRealocated:
				wumpus = random.choice(random_sequency_caves)
				if not wumpus == bats or wumpus == pits:
					isRealocated = True

			#Checking where did the arrow go
			borders = []
			for i in range(1,21):
					if(graph[path[-1]][i] == 1):
						borders.append(i)

			direction_arrow = random.choice(borders)
			#if the direction of the arrow went to the direction of the path, you DIE.
			if direction_arrow in path:
				print("The arrow kill you! GAME OVER")
				game_over = True
			else:
				print("the arrow went away! YOU SAFE.")	

			