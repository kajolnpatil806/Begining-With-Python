low = int(input("Enter the starting value of the range: "))
high = int(input("Enter the ending value of the range: "))

print("Please think of a number between {} and {}.".format(low, high))
input("Press ENTER to start the game.")

guesses = 1
while True:
    middle = low + (high - low) // 2
    high_low = input(
        "My guess is {}. Is it correct (c) or should I guess higher (h) or lower(l): ".format(middle)).casefold()
    if high_low == "h":
        low = middle + 1
    elif high_low == "l":
        high = middle - 1
    elif high_low == "c":
        print("I got the answer in {} guesses.".format(guesses))
        break
    else:
        print("Please print among these options only (h, l or c): ")

    guesses = guesses + 1
