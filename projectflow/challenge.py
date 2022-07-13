Activities = ["Go jogging", "Eat bread", "Laundry",
              "Use Computer", "Code", "Drink", "Dance"]
order = 0

print("Please choose your option from the list below")
for item in Activities:
    print("{} {}".format(order, Activities[order]))
    order += 1


while True:
    choice = int(input("Please select the number an activity you'd like to do: "))

    if 0 <= choice < order:
        print("You've selected {}".format(Activities[choice]))
    else:
        print("Please select a number in the range")
        print("**********************************")
        order = 0
        for item in Activities:
            print("{} {}".format(order, Activities[order]))
            order += 1