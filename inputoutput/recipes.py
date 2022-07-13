import shelve

blt = ["Bacon", "Lettuce", "Tomato", "Bread"]
blt2 = ["Bacon2", "Lettuce", "Tomato", "Bread"]
blt3 = ["Bacon3", "Lettuce", "Tomato", "Bread"]
blt4 = ["Bacon4", "Lettuce", "Tomato", "Bread"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["blt2"] = blt2
    # recipes["blt3"] = blt3
    # recipes["blt4"] = blt4
    # recipes["blt"].append("EGG")
    # recipes["blt2"].append("EGG2")
    #
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # recipes["blt4"].append("Croutons")

    recipes["blt"] = blt
    blt.append("Butter")
    recipes.sync()

    for snack in recipes:
        print(snack, recipes[snack])