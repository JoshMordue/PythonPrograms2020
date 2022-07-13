available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mousemat",
                   "HDMI"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choice = []

for i in range(1, len(available_parts) + 1):
    valid_choice.append(str(i))
print(valid_choice)


current_choice = "-"
computer_parts = [] #create an empty list

while current_choice != '0':
    if current_choice in valid_choice:

        index = int(current_choice) - 1
        current_choice = available_parts[index]
        if current_choice in computer_parts:
            computer_parts.remove(current_choice)
            print("Removing {}".format(current_choice))
        else:
            computer_parts.append(current_choice)
            print("adding {}".format(current_choice))
        print("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)

