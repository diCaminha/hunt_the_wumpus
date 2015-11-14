import random
# Creates a list containing 20 lists initialized to 0
graph = [[0 for x in range(21)] for x in range(21)] 

counterLinks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

count = 50




#creating a random sequency of caves
#the logic is gets a random number between 1 and 20 and then put in the random_sequency_caves, creating a random sequency
random_sequency_caves = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,21):
	done = False
	while not done:
		random_cave = random.randrange(1,21)
		if not random_cave in random_sequency_caves:
			random_sequency_caves[i] = random_cave
			done = True


'''
	Using the random_sequency_caves I did the connections following this logic:
		1. Starting from the firts element in random_sequency_caves, I connect it with the following 3 caves in its front.
			so, suppose the random_sequency_caves is (8,16,18,20,10,3,6,14,9,1,19,7,5,13,17,2,15,11,12,4)
			then, the 8 will be linked to 16,18 and 20.
			The connection will only be accepted if the both current cave and the cave that it is being connected don't have yet 3 connection. 
			Once one of them has 3, any connection will be created. 
			
'''


for i in range(1,21):
	if(counterLinks[random_sequency_caves[i]] < 3):
		graph[random_sequency_caves[i]][random_sequency_caves[i+1]] = 1
		graph[random_sequency_caves[i+1]][random_sequency_caves[i]] = 1
		counterLinks[random_sequency_caves[i]]+=1
		counterLinks[random_sequency_caves[i+1]]+=1
	if(counterLinks[random_sequency_caves[i]] < 3):
		graph[random_sequency_caves[i]][random_sequency_caves[i+2]] = 1
		graph[random_sequency_caves[i+2]][random_sequency_caves[i]] = 1
		counterLinks[random_sequency_caves[i]]+=1
		counterLinks[random_sequency_caves[i+2]]+=1
	if(counterLinks[random_sequency_caves[i]] < 3):
		graph[random_sequency_caves[i]][random_sequency_caves[i+3]] = 1
		graph[random_sequency_caves[i+3]][random_sequency_caves[i]] = 1
		counterLinks[random_sequency_caves[i]]+=1
		counterLinks[random_sequency_caves[i+3]]+=1

#testing choosing rooms
game_over = False
while not game_over:
	option = int(input("enter the number of the option you want\n"
		+"1. choose a room to go\n"
		+"2. guess where's the wumpus\n"))
	if option == 1:
		curently_room = int(input("choose a room: "))
		print("you are in ",curently_room)
		print("you can move to: ")
		for i in range(1,21):
			if(graph[curently_room][i] == 1):
				print(i,end=' ')
		print()
