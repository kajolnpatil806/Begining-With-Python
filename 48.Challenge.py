answer = 5
guess = int(input("Please enter a value: "))

if guess == answer:
    print("You guessed it right the first time.")
else:
    if answer > guess:
        print("Please guess a greater value.")
    else:
        print("Please guess a smaller value.")

    guess = int(input("Enter the value to guess again: "))
    if guess == answer:
        print("You guess it right this time.")
    else:
        print("You are out.")