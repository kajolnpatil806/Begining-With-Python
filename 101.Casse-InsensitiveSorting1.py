pangram = "The brown fox quickly jumps over a lazy dog."
sortedLetters = sorted(pangram)
print("The alphabetically sorted list: ")
print(sortedLetters)

missingLetter = sorted("The quick brown fox jumped over the lazy dog.", key=str.casefold)
print("Printing Missing Letter: ")
print(missingLetter)
print()

numbers = [2.3, 4.3, 4.2, 1.0, 2.3, 4, 43]
sortedNumbers = sorted(numbers)
print("The sorted list of number: ")
print(sortedNumbers)
print("Printing original List: ")
print(numbers)
reversedSorting = numbers
reversedSorting.sort(reverse=True)
print("Printing reverse list using "".sort"" function: ")
print(reversedSorting)
print()

name = ["Kajol", "Nikhil", "Nitin", "Vanita", "vanita", "Ashok", "deepak", "Lochan"]
dotSortNames = name
dotSortNames.sort()
print("Printing .sort names: \n{}".format(dotSortNames))
print()
dotSortNamesKey = name
dotSortNamesKey.sort(key=str.casefold)
print("Printing .sort names with key: \n{}".format(dotSortNamesKey))
