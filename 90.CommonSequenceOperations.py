even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print("Printing minimum even value: {}".format(min(even)))
print("Printing maximum even Value: {}".format(max(even)))
print()
print("Printing minimum odd value: {}".format(min(odd)))
print("Printing maximum odd value: {}".format(max(odd)))
print()
print("Print length of even numbers list: {}".format(len(even)))
print("Print lenght od odd numbers list: {}".format(len(odd)))
print()

word = input("Enter a word: ")
letter = input("Enter the letter you want to search: ")
print("Count the number of letter {} in {}: {}".format(letter, word, word.count(letter)))