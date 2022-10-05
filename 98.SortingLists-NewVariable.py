even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print("Printing the merged List: ")
print(even)
anotherEven = even
print("Printing anotherEven: ")
print(anotherEven)
print()

even.sort(reverse=False)
print("Printing List in ascending order: ")
print(even)
print("Printing anotherEven in ascending order: ")
print(anotherEven)
print()

even.sort(reverse=True)
print("Printing list in descending order: ")
print(even)
print("Printing anotherEven in ascending order: ")
print(anotherEven)

