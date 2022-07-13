# import time
#
# print("The Epoch of this systemstarts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current time is {0}".format(time.tzname[0], time.timezone))
#
#
# if time.daylight != 0:
#     print("\t is in effect")
#     print("The DST timezone is: "+ time.tzname[1])
#
# print("Local time is: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("Local time is: " + time.strftime('%Y-%m-%d %H:%M:%S', time.utc))

# import datetime
#
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())


# userdata = {"swimming": 1000, "running": 6, "jogging": 30}
# template = {"swimming": 7, "running": 2, "jogging": 300}
# combined = {}
# highest = ""
#
# for value, key in userdata.items():
#     if abs(next(iter(userdata[value]))) >= abs(next(iter(userdata[value]))):
#         continue
#     combined[value] = (userdata[value] - template[value])
#
# print(next(iter(combined)))
#
# print(combined)

# combined = sorted(combined, reverse=True, key=lambda dict_key: abs(combined[dict_key]))
#first entry is swimming, jogging, running

# while x < str
#
# for value in enumerate(userdata):
#     userdata[key] -= template[key]
#
# absValues = [abs(number) for number in userdata]


#sorted(absValues, key=itemgetter(1))
import numpy as np

userdata = [100000000, 6, 300000]
template = [7000, 2, 300]
combined = [0,0,0]
x = 0
pointer = 0

while x < len(userdata):

    combined = (userdata[x] - template[x])

    combined = np.absolute(combined)

    if userdata[x] > userdata[pointer]:
        pointer = x

    x += 1

if pointer == 0:
    print("You're a weird swimmer boy.")

if pointer == 1:
    print("You're a weird jogger boy: let's try to change that.")

if pointer == 2:
    print("You're a weird tennis boy: change.")

if userdata[pointer] < -2 or userdata[pointer] > 2:
    userdata[pointer] *= 0.95

print("Here's your revised plan for the week: Swimming: {} Jogging {} "
      "Running: {} ".format(userdata[0], userdata[1], userdata[2]))



# userdata = [1000, 6, 300000]
# template = [7000, 2, 300]
# combined = []
# x = 0
# pointer = 0
# absolute = 0
#
# while x < len(userdata):
#
#     absolute = abs(userdata[x] - template[x])
#     combined.append(absolute)
#
#     if x > 1:
#         if userdata[x] > userdata[0]:
#             pointer = x
#     x += 1
#
# if pointer == 0:
#     print("You're a weird swimmer boy.")
#
# if pointer == 1:
#     print("You're a weird jogger boy: let's try to change that.")
#
# if pointer == 2:
#     print("You're a weird tennis boy: change.")
#
# if userdata[pointer] < -2 or userdata[pointer] > 2:
#     userdata[pointer] *= 0.95
#
# print("Here's your revised plan for the week: Swimming: {} Jogging {} "
#       "Running: {} ".format(userdata[0], userdata[1], userdata[2]))


