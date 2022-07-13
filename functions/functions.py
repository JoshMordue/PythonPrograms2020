def multiply(x, y):
    """
    Multiply the values entered both x and y
    :param x: The first value to multiply
    :param y: The second value to multiply
    :return: The 'Int' from multiplying x and y
    """
    result = x * y
    return result


def fibonacci(n):
    """Return the 'n'th Fibonacci number, for positive 'n'"""
    if 0 <= n <= 1:
        return n

    n_minus1 = 0
    n_minus2 = 1

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(16):
    print(i, fibonacci(i))


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

test = multiply(6, 6)
print(test)



for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)
