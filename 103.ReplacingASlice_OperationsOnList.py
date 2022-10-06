computerParts = [
    "Monitor",
    "CPU",
    "Mouse",
    "Keyboard",
    "Mouse Mat",
    "HP Printer"
]
print("Printing original list: \n{}".format(computerParts))
print()

# Operation1 = s[i] = x
computerParts[5] = "Dell Printer"
print("Printing Replaced list: \n{}".format(computerParts))
print()

# Operation2 = s[i:j] = [t]
computerParts[4:] = ["External Computer Setup"]
print("Printing list replaced with many numbers: \n{}".format(computerParts))
print()