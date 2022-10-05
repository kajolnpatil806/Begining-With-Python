activity = input("What do you feel like doing today? \n")

if "paint" not in activity.casefold():
    print("But I want to paint today.")
else:
    print("Yes, I want to do the same. ")