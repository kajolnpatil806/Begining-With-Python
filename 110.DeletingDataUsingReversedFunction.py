data = [223, 3434, 12, 23, 123, 23, 12, 122, 125, 134, 145, 199, 121, 111, 1, 3]

minValue = 100
maxValue = 200

top_index = len(data) -1
for index, value in enumerate(reversed(data)):
    if value < minValue or value > maxValue:
        print("Printing the reversed indexes and data that need to be deleted: {}, {}".format(top_index - index, value))
        del data[top_index -index]
print("Printing the final data: {}".format(data))
