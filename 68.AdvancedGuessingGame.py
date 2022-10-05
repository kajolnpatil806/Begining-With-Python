import random
higher = int(input("Set the highest value: "))
answer = random.randint(1, higher)
print(answer)       # TODO: Remove after testing
guess = int(input("Please guess a number between 1 to {}: ".format(higher)))

if guess == answer:
    print("You got it the first time.")
else:
    if guess < answer:
        print("Guess a higher number: ")
    else:
        print("Please guess a lower no: ")
    guess = int(input())

    if guess == answer:
        print("You got it this time.")
    else:
        print("Start the game over.")

