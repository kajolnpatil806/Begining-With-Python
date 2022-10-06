emptyList = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print("Printing numbers = [even,odd]: {}".format(numbers))
print()

for numbersList in numbers:
    print("Printing each element in numbers: {}".format(numbersList))

    for value in numbersList:
        print("Printing value of each number in list: {}".format(value))