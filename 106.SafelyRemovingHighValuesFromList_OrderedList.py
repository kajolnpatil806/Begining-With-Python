# Original Case:
data = [3, 6, 12, 33, 112, 126, 137, 154, 166, 178, 199, 305, 366, 399]
# Case:01- data = [12, 33, 112, 126, 137, 154, 166, 178, 199, 305, 366, 399]
# Case:02- data = [3, 6, 12, 33, 112, 126, 137, 154, 166, 178, 199]
# Case:03- data = [112, 126, 137, 154, 166, 178, 199]
# Case self: data = [1, 2, 3, 4, 5]
# Case:04- data = []

min_value = 100
max_value = 200

# Deleting Low Values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_value:
        stop = index
        break
print("Printing the index position where the stop variable was set: {}".format(stop))
del data[:stop]
print("Printing the List after deleting the necessary data: {}".format(data))
print()

# Deleting high values in list
start = 0
for index in range(len(data)-1, -1, -1):
    if data[index] <= max_value:
        start = index + 1
        break
print("Printing the index position where the start variable was set: {}".format(start))
del data[start:]
print("Printing the List after deleting the necessary data: {}".format(data))