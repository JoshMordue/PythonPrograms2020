# farm_animals = {"Sheep", "Cow", "Hens"}
# print(farm_animals)
# for animal in farm_animals:
#     print(animal)
#
# wild_animals = {"Lion", "Tiger", "Hare"}
#
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("Horse")
# wild_animals.add("Horse")
#
# print(farm_animals)
# print(wild_animals)
#
# empty_set = set()
# empty_set2 = {}
# # empty_set.add("a")
# # empty_set2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4,6,9,16,25,25,25,4)
# squares = set(squares_tuple)
# print(squares)
# even = set(range(0,40,2))
# print(even)
# print(len(even))
#
# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))


#
# even = set(range(0,40,2))
# squares_tuple = (4,6,9,16,25)
#
# print(sorted(even))
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("Even minus square")
#
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print("=" * 40)
# print(sorted(even))
# print(sorted(squares))
# even.difference_update(squares)
# print(sorted(even))



even = set(range(0,40,2))
squares_tuple = (4,6,9,16,25)

print("Symmetric even minus square")
print(sorted(even.symmetric_difference(squares_tuple)))


