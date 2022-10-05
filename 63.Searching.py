shopping_list = ["Milk", "Cornflour", "Eggs", "Fish", "Cheese", "Chocolate"]

item_to_find = "Fish"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index

print("Item found at position {0}.".format(found_at))