numbers = "2,234,234,544,567,566"
print("Print a step in numbers string")
print(numbers[1::4])
print(numbers[1::3])

print()
number = "233;334,12;334;2;3;32"
print("Mixed Seperators")
print(number[1::5])

print()
print("Printing the numbers using seperator Variable")
numberSeperators = "233;334,12;334;2;3;32"
seperators = numberSeperators[1:4]
print(seperators)
