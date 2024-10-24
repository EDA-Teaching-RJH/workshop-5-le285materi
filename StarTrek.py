import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 

		action = get_user_action()

		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
				print(f"Simulation ended. Final score: {score}")
		else: 
			print("Invalid action. Please try again.") 
		
		turns += 1 
		handle_random_event() 

		if turns % 3 == 0: 
			replenish_resources() 

def display_status(): 
	# TODO: Implement function to display ship status, resources, and crew 
      print("Display ship staus, resources, and crew")
def get_user_action(): 
	choice = input("1 run mission \n 2 repair system \n 3 add crew member \n 4 final score")
	return choice 
	
def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

def repair_system(): 
	# TODO: Implement system repair functionality
    print("system and repair code")
def add_crew_member(): 
	# TODO: Implement functionality to add a new crew member 
    print("add a new crew code")
def handle_random_event():
	# TODO: Implement random events that can occur during the simulation 
       print("random events that can occur during the simulation code")
def use_resource(resource, amount): 
	# TODO: Implement resource usage logic 
    print("resources usage and logic code")
def replenish_resources(): 
	# TODO: Implement resource replenishment logic 
      print("resources replenishemnt logic code")
main()