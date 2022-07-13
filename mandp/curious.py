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
# first entry is swimming, jogging, running

# while x < str
#
# for value in enumerate(userdata):
#     userdata[key] -= template[key]
#
# absValues = [abs(number) for number in userdata]
# sorted(absValues, key=itemgetter(1))
import numpy as np

userdata = [10, 10, 10]
template = [10, 10, 10]
x = 0
pointer = 0
combined = np.subtract(userdata, template)
combined = np.absolute(combined)

while x < len(userdata):
    if combined[x] >= combined[pointer]:
        pointer = x

    x += 1

if userdata[pointer] - template[pointer] <= -2:
    userdata[pointer] *= 1.05
elif userdata[pointer] - template[pointer] >= 2:
    userdata[pointer] *= 0.95
else:
    print("No changes need to be made. Good job :)")
    exit()

if pointer == 0:
    print("You're a weird swimmer boy.")

if pointer == 1:
    print("You're a weird jogger boy: let's try to change that.")

if pointer == 2:
    print("You're a weird tennis boy: change.")

print("Here's your revised plan for the week: Swimming: {} Jogging {} "
      "Running: {} ".format(userdata[0], userdata[1], userdata[2]))


#
# import numpy as np
#
# userdata = [100000000, 6, 300000]
# template = [7000, 2, 300]
# x = 0
# pointer = 0
#
# while x < len(userdata):
#
#     userdata[x] -= template[x]
#
#     userdata = np.absolute(userdata)
#
#     if userdata[x] > userdata[pointer]:
#         pointer = x
#
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
