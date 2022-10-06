data = [3, 6, 12, 33, 112, 126, 137, 154, 166, 178, 199, 305, 366]

minValue = 100
maxValue = 200

# Code For Lower Value
stop = 0
for index, value in enumerate(data):
    if value >= minValue:
        stop = index
        break

print("Printing the index psotion where the stop variable was set: {}".format(stop))
del data[:stop]
print("Printing the List after deleting the necessary data: {}".format(data))