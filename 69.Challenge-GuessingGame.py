import random
higher = int(input("Choose the higher value: "))
answer = random.randint(1, higher)
print(answer)
guess = int(input("Please guess a number between 1 and {}: ".format(higher)))

while guess != answer:

    if guess == 0:
        print("You quit.")
        break

    if guess == answer:
        print("Congratulations! you guessed it correct the first time.")
        break
    else:
        if guess < answer:
            print("Try again with a higher number: ")
        else:
            print("Try again with a lower number: ")
        guess = int(input())
        if guess == answer:
            print("Congratulations! You got it this time.")

