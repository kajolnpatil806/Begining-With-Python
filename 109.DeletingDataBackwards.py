data = [223, 3434, 12, 23, 123, 23, 12, 122, 125, 134, 145, 199, 121, 111, 1, 3]

minValue = 100
maxValue = 200

for index in range(len(data)-1, -1, -1):
    if data[index] < minValue or data[index] > maxValue:
        print("Printing original index and data: {}, {}".format(index,data))
        del data[index]
print("Printing the final data: {}".format(data))
