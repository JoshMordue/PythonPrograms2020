import shelve

# with shelve.open('shelvetest') as fruit:
fruit = shelve.open('shelvetest')
# fruit['orange'] = 'ORANGE'
# fruit['apple'] = 'APPLE'
# fruit['lemon'] = 'LEMON'
# fruit['grape'] = 'GRAPE'

# print(fruit["lemon"])
# print(fruit["orange"])
#
# fruit["grape"] = "GRAPES"
#
# for snack in fruit:
#     print(snack + " " + fruit[snack])

# while True:
#     shelf_key = input("Please enter a fruit: ").lower()
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "We don't have a " + shelf_key)
#     print(description)

# ordered_keys = sorted(list(fruit.keys()))
#
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())


fruit.close()