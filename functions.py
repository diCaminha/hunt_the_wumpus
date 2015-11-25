import random
#Function to generate a randomly sequence of caves 
all_caves = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random_sequency_caves = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def create_randomSequency_caves():
	for i in range(1,21):
		cave = random.choice(all_caves)
		all_caves.remove(cave)
		random_sequency_caves[i] = cave
	random_sequency_caves.remove(0)
	return random_sequency_caves