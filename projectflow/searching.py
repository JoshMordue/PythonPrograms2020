shopping_list = ["milk", "pasta",  "eggs", "spam", "bread", "rice"]
item_to_find = "spam"
found_at = None

# for item in shopping_list:
#     if item == "spam":
#         print("Found spam! at location {} in the array".format(found_at))
#     found_at = found_at + 1

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
#


if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Found spam! at location {} in the array".format(found_at))
else:
    print("Could not find matching item in the array")