data = [564,321,5,48,984,655132,1654,8974,
        65,654,4784,62,1321,56,9854]

min_valid = 100
max_valid = 400
#
# for index in range(len(data)-1,-1,-1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)

top_index = len(data) - 1

for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]


