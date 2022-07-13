def multiply(x, y):
    """
    Multiply the values entered both x and y
    :param x: The first value to multiply
    :param y: The second value to multiply
    :return: The 'Int' value from multiplying x and y
    """
    result = x * y
    return result


def palindrome(string: str) -> bool:
    """
    Get a String from Standard Input (stdin) to ascertain whether
    the String is a palindrome.

    The function will firstly separate any spaces from the string.

    It will then assign the variable "Iter" the value of half the
    number of characters entered (Due to not requiring half the
    characters tested).
    The 'I' variable is assigned for matching the first character of the
    String with the last character 'J'.

    It will then loop to compare the letters whilst incrementing &
    decrementing until it reaches the middle character (Iters value)

    :param string: The sentence to check.

    :return: True or False whether the entered 'String' is a
        Palindrome
    """
    string = string.replace(" ", "")

    iter = int(len(string) / 2)
    # number of cycles to check that if it is a palindrome
    i = 0 # first character index
    j = int(len(string) - 1) #last character index

    for letter in range(i, iter):
        if string[i] == string[j]:
            j -= 1
            i += 1
    if i == iter:
        return True


word = input("Please enter a word to check: ").casefold()


if palindrome(word):
    print("{} is a palindrome".format(word))
else:
    print("{} Is not a palindrome".format(word))


