def sum_numbers(*values: float)-> float:
    """Returns the value of all the variables added"""
    result = 0

    for numbers in values:
        print(numbers)
        result += numbers
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(12.5, 2.2, 5.5))