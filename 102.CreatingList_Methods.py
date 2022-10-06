emptyList = []
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

number = even + odd
print("Printing added numbers: {}".format(number))
print()

sortedNumbers = sorted(number)
print("Printing sortedNumbers : {}".format(sortedNumbers))
print()

digits = sorted("2323235dsfbjhdf")
print("Printing sorted list with random characters: {}".format(digits))
print()

digitsToCheckSorted = sorted("25824312asjlfp")
print("Printing digits to see the sorted list of items: {}".format(digitsToCheckSorted))
digitsToCheckInList = list("25824312asjlfp")
print("Printing digits to check the series of character converted in List: {}".format(digitsToCheckInList))
print()

more_digitsToCheckInList = list(digitsToCheckInList)
print("Printing the check sorted list using another variable: {}".format(more_digitsToCheckInList))
print()

print("Checking if more_digitsToCheckInList is same as digitsToCheckInList: {}".format(
    more_digitsToCheckInList is digitsToCheckInList))
print("Checking if more_digitsToCheckInList is equal to digitsToCheckInList: {}".format(
    more_digitsToCheckInList == digitsToCheckInList))
print()

print("Printing original List: {}".format(number))
copyingNumber = number[:]
print("Printing copied list using Slice method: {}".format(copyingNumber))
print()

print("Printing original List: {}".format(number))
dotCopyMethod = number.copy()
print("Printing copied list by .copy method: {}".format(dotCopyMethod))
print()
