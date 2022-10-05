name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))
print(name + " is {0} years old.".format(age))

if age >= 18:
    print("She is eligible to vote")
    print("Please put an X in the box.")
else:
    print("Please come back in {0} years to vote.".format(18-age))
