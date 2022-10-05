availableParts = [
    "Monitor",
    "CPU",
    "Mouse",
    "Keyboard",
    "Mouse Mat",
    "HDMI Cable",
    "Printer"
]

validChoices = []
for i in range(1, len(availableParts) + 1):
    validChoices.append(str(i))
print(validChoices)
currentChoice = "-"
computerParts = []

while currentChoice != '0':
    if currentChoice in "1234567":
        index = int(currentChoice) - 1
        chosenPart = availableParts[index]
        if chosenPart in computerParts:
            print("Removing the {} item from the cart.".format(currentChoice))
            computerParts.remove(chosenPart)

        else:
            print("Adding item {} in the cart.".format(currentChoice))
            computerParts.append(chosenPart)

    else:
        print("Please add options from the list below: ")
        for number, parts in enumerate(availableParts):
            print("{0}: {1}".format(number + 1, parts))

    print()
    currentChoice = input("Enter the item code to add/remove the items from the cart: ")

print()
print("You final items in the cart are: {}".format(computerParts))

