'''
Challenge 01: Add some code to program, so that it prints out we win.
Each character should appear on a seperate line.
The  program should get the characters from the parrot string, using indexing.
The final output should look like:
w
e

w
i
n
'''

parrot = "Norwegian Blue"

print("Regular Index")
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print("Negative Index")
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print("Formula Based Indexing")
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

