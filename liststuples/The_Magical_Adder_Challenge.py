numbers = input("Please input three numbers you wish to be added Separated by , : ")

str_numbers = numbers.split(",")

for index in range(len(str_numbers)):
    str_numbers[index] = int(str_numbers[index])

final = str_numbers[0] + str_numbers[1] - str_numbers[2]

print(final)

5



