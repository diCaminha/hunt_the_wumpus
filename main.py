import random
# Creates a list containing 20 lists initialized to 0
graph = [[0 for x in range(21)] for x in range(21)] 

counterLinks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

count = 50


'''
	The logic of finding 3 edges randomically for each room was breaking down in 3 for loops.
		Where the first for will only let create a edge between the current room (i) and the random room (randomNumber) if 
	both have no edges yet.
	In the second for loop is the same logic. Only creates the edge if both candidates rooms have 1 edges. And finally for the last for loop,
	will create a edge if both room candidates have 2 edges.
		That is pretty much forcing, in each for loop, all the rooms have the same number of edges. Avoind the problem before. where
		in some point, we're trying to find a edge for a room and all the others have already 3 edges.
'''

'''
	Problems:
		Running some times, I faced this problem:
		-> Okay, in the first forloop the code found for all the rooms a other room. then, each room has 1 edge. 
		-> BUT, in the second forloop, the last two rooms missing a edge(the only two rooms with only 1 edge) were already connected
			in the first forloop!!! So, they cannot be connected anymore! Then, the INFINITE LOOP HAPPENS AGAIN.
'''


#first loop to fill out the first edge for all rooms
for i in range(1, 21):
	
	done = False
	while not done:
		if counterLinks[i] != 0:
			done = True
		else:
			randomNumber = random.randrange(1,21)
			if counterLinks[randomNumber] == 0 and graph[i][randomNumber] == 0 and randomNumber != i: 
				graph[i][randomNumber] = 1
				graph[randomNumber][i] = 1
				counterLinks[i]+=1
				counterLinks[randomNumber]+=1
				done = True
				print (i,randomNumber);

#second loop to fill out the second edge for all rooms
for i in range(1, 21):
	
	done = False
	while not done:
		if counterLinks[i] != 1:
			done = True
		else:
			randomNumber = random.randrange(1,21)
			if counterLinks[randomNumber] == 1 and graph[i][randomNumber] == 0 and randomNumber != i: 
				graph[i][randomNumber] = 1
				graph[randomNumber][i] = 1
				counterLinks[i]+=1
				counterLinks[randomNumber]+=1
				done = True
				print (i,randomNumber);

#third loop to fill out the third edge for all rooms
for i in range(1, 21):
	
	done = False
	while not done:
		if counterLinks[i] != 2:
			done = True
		else:
			randomNumber = random.randrange(1,21)
			if counterLinks[randomNumber] == 2 and graph[i][randomNumber] == 0 and randomNumber != i: 
				graph[i][randomNumber] = 1
				graph[randomNumber][i] = 1
				counterLinks[i]+=1
				counterLinks[randomNumber]+=1
				done = True
				print (i,randomNumber);
		


for i in range(1,21):
	for j in range(1,21):
		print(graph[i][j], end=' ')
	print()	


#testing choosing rooms

curently_room = int(input("choose a room"))
print("you are in ",curently_room)
print("you can move to: ")
for i in range(1,21):
	if(graph[curently_room][i] == 1):
		print(i,end=' ')
print()
