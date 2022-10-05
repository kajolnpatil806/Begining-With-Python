age = int(input("Please enter your age: "))
print()
print("AND Condition.")
# if age >= 16 and age <= 65:
# can also be done in a following way:
# if age in range(16, 66):
if 16 <= age <= 65:                 # Simplified equation
    print("Have a good day at work.")
else:
    print("Enjoy your free time.")
print()
print("_" * 80)
print()








print("OR Condition.")
if age < 16 or age > 65:
    print("Enjoy your free time.")
else:
    print("Have a good day at work.")
