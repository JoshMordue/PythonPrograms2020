menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#
#     for item in meal:
#         print(item)
#     else:
#         print("{0} has a spam score of {1}"
#               .format(meal, meal.count("spam")))

# empty_menu=[]
#
# for meal in menu:
#
#     for item in meal:
#         if item != "spam":
#             (print(item, end=", "))
#
#     print()


# for meal in menu:
#
#     for item in meal:
#         if item != "spam":
#             empty_menu.append(item)
#
#
# print(empty_menu)
#
for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))








