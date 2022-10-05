age = 24
print("Method 1:")
print("My age is " + str(age) + "-years.")
print()

print("Method 2:")
print("My age is {0} years".format(age))
print()

print("All in one.")
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "January", "March", "May", "July", "August", "October", "December"))
print()

print("Method 2:")
print("There are {0} days in January, March, May, July, August, October, December".format(31))
print()

print("Method 3:")
print("Days in January are {1}.\n Days in February are {0}.\n Days in March are {1}.\n "
      "Days in April are {2}.\n Days in May are {1}.\n Days in June are {2}.\n "
      "Days in July are {1}.\n Days in August are {1}.\n Days in September are {2}.\n "
      "Days in October are {1}.\n Days in Noveber are {2}.\n Days in December are {1}.\n"
      .format(28, 31, 30))
print()

print("Method 4:")
print("""Days in January are {1}.
Days in February are {0}.
Days in March are {1}.
"Days in April are {2}.
Days in May are {1}. 
Days in June are {2}.
Days in July are {1}. 
Days in August are {1}.
Days in September are {2}.
Days in October are {1}. 
Days in Noveber are {2}. 
Days in December are {1}.
"""
      .format(28, 31, 30))