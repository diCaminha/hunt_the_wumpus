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