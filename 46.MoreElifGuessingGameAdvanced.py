answer = 5
guess = int(input("Please enter a number to guess: "))

# Organized
if guess != answer:
    if guess < answer:
        print("Please guess a greater value.")
    else:
        print("Please guess a lower value.")

    guess = int(input("Guess a number again: "))
    if guess == answer:
        print("You guessed it right.")
    else:
        print("You guessed it wrong.")

else:
    print("You got it the 1st time.")


# Unorganized
# if guess < answer:
#     print("Please guess higher value.")
#     guess = int(input())
#     if guess == answer:
#         print("You guess it correct.")
#     else:
#         print("Sorry, you guessed it wrong.")
# elif guess > answer:
#     print("Please guess the lower value.")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it correct")
#     else:
#         print("Sorry you guessed it wrong.")
# else:
#     print("You are correct the first time.")