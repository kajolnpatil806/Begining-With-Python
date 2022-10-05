if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")

# can also use
# if name:
if name != "":
    print("Hello, {}.".format(name))
else:
    print("Are you a man with no name?")