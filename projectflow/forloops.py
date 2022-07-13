parrot = "Norwegian Blue"

for character in parrot:
    print(character)


number = input("Please enter a series of numbers: ")
seperators = ""

for char in number:
    if not char.iscapital():
        seperators = seperators + char


print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))

