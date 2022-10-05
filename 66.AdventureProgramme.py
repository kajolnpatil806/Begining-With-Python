available_exit = ["north", "south", "east", "west"]

chosen_exit = input("Choose a Direction: ")

while chosen_exit not in available_exit:
    chosen_exit = input("Please choose a different direction: ")

print("You are finally out. ")
