fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg={"Cabbage": "Every child's Favourite",
     "Sprouts": "Mmmmm Lovely",
     "Spinach": "Can i have some more fruit please?"}

print(veg)

veg.update(fruit)
print(veg)

print(fruit)

nice = fruit.copy()
nice.update(veg)
print(nice)
print(veg)
print(fruit)