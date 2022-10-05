letter = "abcdefghijklmnopqrstuvwxyz"
backwards = letter[25:0:-1]
print("With zero:")
print(backwards)
print()

print("With -1:")
backwards1 = letter[25:-1:-1]
print(backwards1)
print()

print("With nothing")
backwards2 = letter[25::-1]
print(backwards2)