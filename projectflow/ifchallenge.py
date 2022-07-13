name = input("What's your name? ")
age = int(input("How old are you {}? ".format(name)))

if 18 <= age < 31:
    print("welcome to the holiday son")
else:
    print("Grow up! or down!")