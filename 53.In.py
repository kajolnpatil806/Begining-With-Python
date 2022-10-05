inputName = input("Enter a string you need to check for: ")
letter = input("Enter the letter you want to check for: ")

if letter in inputName:
    print("{} is in {}.".format(letter, inputName))
else:
    print("Character/s not found.")