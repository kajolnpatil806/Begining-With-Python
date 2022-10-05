name = input("Enter your name: ")
age = int(input("Hi {0}, Enter your age: ".format(name)))
print("{0} is {1} years old.".format(name, age))
print()

if age < 18:
    print("Please come back after {0} years.".format(18-age))

elif age == 900:
    print("Sorry, {0}, you die in return of the Jodi.".format(name))

else:
    print("You are old enough to vote.")
    print("PLease put an X in the box.")