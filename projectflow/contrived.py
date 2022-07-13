numbers =[1, 45, 31, 12, 60]


for number in numbers:
    if number % 8 == 0:
        print("the numbers are unacceptable")
        break

else:
    print("all numbers are fine")