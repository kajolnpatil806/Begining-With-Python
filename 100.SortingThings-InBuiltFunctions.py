pangram = "The brown fox quickly jumps over a lazy dog."
sortedLetters = sorted(pangram)
print("The alphabetically sorted list: ")
print(sortedLetters)
print()

numbers = [2.3, 4.3, 4.2, 1.0, 2.3, 4, 43]
sortedNumbers = sorted(numbers)
print("The sorted list of number: ")
print(sortedNumbers)
print()

print("Printing original List: ")
print(numbers)
print()

reversedSorting = numbers
reversedSorting.sort(reverse=True)
print("Printing reverse list using "".sort"" function: ")
print(reversedSorting)