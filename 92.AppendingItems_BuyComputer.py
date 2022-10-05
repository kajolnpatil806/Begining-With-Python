currentChoice = "-"
computerParts = []

while currentChoice != '0':
    if currentChoice in "123456":
        print("Adding item {} in the cart.".format(currentChoice))

        if currentChoice == '1':
            computerParts.append("Monitor")

        elif currentChoice == '2':
            computerParts.append("CPU")

        elif currentChoice == '3':
            computerParts.append("Mouse")

        elif currentChoice == '4':
            computerParts.append("Keyboard")

        elif currentChoice == '5':
            computerParts.append("Mouse Mat")

        elif currentChoice == '6':
            computerParts.append("HDMI Cable")

    else:
        print("Please add options from the list below: ")
        print("Enter 1: Monitor")
        print("Enter 2: CPU")
        print("Enter 3: Mouse")
        print("Enter 4: Keyboard")
        print("Enter 5: Mouse Mat")
        print("Enter 6: HDMI Cable")
        print("Enter 0: To finish")

    print()
    currentChoice = input("Enter the item code to add in cart: ")

print()
print("You final items in the cart are: {}".format(computerParts))

