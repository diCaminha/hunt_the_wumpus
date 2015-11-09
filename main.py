import random
# Creates a list containing 5 lists initialized to 0
graph = [[0 for x in range(21)] for x in range(21)] 

counterLinks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#for all the rooms choose 3 randomly
for i in range(1, 21):
	while(counterLinks[i] < 3):
		randomNumber = random.randrange(1,21)
		if counterLinks[i] < 3 and counterLinks[randomNumber] < 3 and graph[i][randomNumber] == 0 and randomNumber != i: 
			graph[i][randomNumber] = 1
			graph[randomNumber][i] = 1
			counterLinks[i]+=1
			counterLinks[randomNumber]+=1
			



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