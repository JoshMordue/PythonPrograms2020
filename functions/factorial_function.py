# def factorial_function(multiplier : int):
#     """
#     This program prints the factorial numbers of numbers between 1-35
#     It goes through the loop multiplying 'ANSWER' and 'Multiplier' and
#     to print a result - then incrementing 'Multiplier' to times the
#     answer again.
#     :param multiplier: The multiplier used to get the factorial of
#     each number, incrementing by one every parse.
#     :return: None - instead prints out the multiplier used and the
#     answer value that it was times by.
#     """
#     ANSWER = 1
#     multiplier: int = 1
#
#     for i in range(multiplier, 36):
#         ANSWER = multiplier * ANSWER
#         multiplier += 1
#         print(multiplier, " ", ANSWER)
#
#
# factorial_function(1)


def factorial(n: int) -> int:
     """Return n! (0! is 1)."""
     if n <= 1:
         return 1

     result = 2
     for x in range(3, n + 1):
         result *= x

     return result


for i in range(36):
     print(i, factorial(i))
