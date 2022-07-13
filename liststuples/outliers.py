data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# del data[0:5]
# print(data)
# del data[10:]
# print(data)

min_valid = 5
max_valid = 15
deletion = []


# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
#
# print(stop)
# del data[:stop]
# print(data)
#
# start = 0
# for index in range(len(data) -1, -1, -1):
#     print(data[index])
#     if data[index] <= max_valid:
#         start = index+1
#         break
# del data[start:]
# print(data)

stop = 0

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
del data[:stop]

start = 0

for index in range(len(data)-1,-1,-1):
    if data[index] <= max_valid:
        start = index + 1
        break

del data[start:]





print(data)
