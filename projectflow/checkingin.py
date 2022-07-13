parrot = "Norwegian Blue"

letter = input("Enter a character :")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("There is no such letter.")