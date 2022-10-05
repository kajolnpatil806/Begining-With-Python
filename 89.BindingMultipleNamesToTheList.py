shopping_list = [
    "Foundation",
    "Eye Liner",
    "Kajal",
    "Lipstick",
    "Blush"
]
another_List = shopping_list
print("Original Shopping List: {}".format(shopping_list))
print(id(shopping_list))
print(id(another_List))
print()

shopping_list += ["Highlighter"]    # Augmented Assignment
print("New Shopping list: {}".format(shopping_list))
print(id(shopping_list))
print("Another List Print: {}".format(another_List))
print(id(another_List))
print()

a = b = c = d = e = f = another_List
print("Printing A: {}".format(a))

print("Adding Cream")
b.append("Contour")
print("Print C: {}".format(c))
print("Print D: {}".format(d))