available_exit = ["east", "west", "north", "south"]

choose_exit = input("Please enter the direction to exit: ")

while choose_exit not in available_exit:
    choose_exit = input("Please enter another direction: ")
    if choose_exit.casefold() == "quit":
        print("You Quit.")
        break

else:
    print("Wohoo, you got out of the game.")