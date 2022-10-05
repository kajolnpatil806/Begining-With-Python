parrot = "Norwegian Blue"
print("First- With Start and Stop Index, start from 0.")
print(parrot[0:6])  # From 0 to 6 but do not include 6

print(" ")
print("Second- With Start and Stop index, Random numbers.")
print(parrot[3:8])  # From 3 to 8 but do not include 8

print()
print("Third- With start and stop index from 2nd word of the string.")
print(parrot[10:14])

print()
print("Forth- Not putting stop index")
print(parrot[0:])

print()
print("Fifth- Adding/Concatenating the Sliced letters")
print(parrot[3:6] + parrot[10:13])

print()
print("Sixth- Only colons in the square bracket.")
print(parrot[:])