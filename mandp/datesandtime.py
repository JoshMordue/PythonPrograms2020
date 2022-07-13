# import time
# import calendar
#
# print(time.gmtime(0))
#
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)
# print(time_here[3])
# print(time_here[4])

import time
from time import perf_counter as my_timer
import random

input("Press Enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)

start_time = my_timer()
input("Please press Enter to stop")

end_time = my_timer()

print("Started at: " + time.strftime("%X", time.localtime(start_time)))
print("Ended at: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} Seconds".format(end_time - start_time))
























#sorted(absValues, key=itemgetter(1))
import numpy as np

userdata = [100000000, 6, 300000]
template = [7000, 2, 300]
x = 0
pointer = 0

while x < len(userdata):

    userdata[x] -= template[x]

    userdata = np.absolute(userdata)

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
