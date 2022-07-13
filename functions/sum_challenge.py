def sum_eo(num, pref):
    # if pref == "E":
    #     print("The even numbers from 0 to {}".format(num))
    #     for number in range(2,num, 2):
    #         print(number)
    #
    # if pref == "O":
    #     for number in range(1,num, 2):
    #         print(number)
    #         return
    # else:
    #     print("-1")
    #

    if pref == "E":
        start = 2
    elif pref == "O":
        start = 1
    else:
        return -1

    return sum(range(start, num, 2))


n =  int(input("Please input the number: "))
t =  input("Please input odd or even: ").upper()


result = sum_eo(n, t)
print(result)

