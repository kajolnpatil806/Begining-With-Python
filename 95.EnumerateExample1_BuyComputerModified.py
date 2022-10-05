availableParts = [
    "Monitor",
    "CPU",
    "Mouse",
    "Keyboard",
    "Mouse Mat",
    "HDMI Cable",
    "Printer"
]
currentChoice = "-"
computerParts = []

while currentChoice != '0':
    if currentChoice in "1234567":
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

        elif currentChoice == '7':
            computerParts.append("Printers")

    else:
        print("Please add options from the list below: ")
        for number, parts in enumerate(availableParts):
            print("{0}: {1}".format(number + 1, parts))

    print()
    currentChoice = input("Enter the item code to add in cart: ")

print()
print("You final items in the cart are: {}".format(computerParts))

