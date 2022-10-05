name = input("Please enter you name: ")
age = int(input("Please enter your age: "))

if 18 <= age <= 30:
    print("Welcome to your holiday destination.")
else:
    if age < 18:
        print("Please come back in {} years.".format(18-age))
    else:
        print("You are over age for this activity.")