import string


def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return "pass"


input("Play Fizz Buzz. Press ENTER to start")
print("*" * 50)
print()

next_number = 1


while next_number < 101:
    print("The number is {0}".format(next_number))

    answer = input("'Fizz', 'Buzz', 'Fizz Buzz' or 'Pass': ").casefold()
    if (fizz_buzz(next_number)) == answer:
        print("That's the correct answer - Now the computer's turn!")
        next_number += 1
        print("*" * 50)
    else:
        print("You lost good job")
        exit()
    print("The number is {0}".format(next_number))
    print("The computer has guessed {}".format(fizz_buzz(next_number)))
    print("That's the correct answer - Now it's your turn!")
    print("*" * 50)
    next_number += 1




    #check to see the right answer to the number
    #compare it with the users one
    #if true computers turn







