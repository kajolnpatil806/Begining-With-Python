shopping_list = [
    "Foundation",
    "Eye Liner",
    "Kajal",
    "Lipstick",
    "Blush"
]
print("Original Shopping List: {}".format(shopping_list))
another_List = shopping_list
print(id(shopping_list))
print(id(another_List))
print()

shopping_list += ["Highlighter"]    # Augmented Assignment
print("New Shopping list: {}".format(shopping_list))
print(id(shopping_list))
print(id(another_List))