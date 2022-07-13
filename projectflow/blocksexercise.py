name = input("please enter your name: ")
age = int(input("Please enter your age {0}: ".format(name)))
print(age)

if age >= 18:
    print("Congratulations! you can vote")
else:
    print("Too young! GROW UP! Come back in {0} Years".format(18 - age))