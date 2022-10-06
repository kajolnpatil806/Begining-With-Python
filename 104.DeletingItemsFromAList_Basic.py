data = [3, 6, 112, 126, 137, 178, 199, 305, 366]
print("Printing original data: {}".format(data))

min_value = 100
max_value = 200
del data[0:2]
print("Printing deleted data: {}".format(data))
del data[5:]
print("Printing after deleting the 2nd time: {}".format(data))
