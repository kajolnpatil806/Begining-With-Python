shopping_list = ["Milk", "Cornflour", "Eggs", "Fish", "Cheese", "Chocolate"]

# for item in shopping_list:
#     if item != "Fish":
#         print("Buy " + item)

for item in shopping_list:
    if item == "Fish":
        continue

    print("Buy " + item)