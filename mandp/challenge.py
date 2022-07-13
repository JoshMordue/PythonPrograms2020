# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.
#
# from time import perf_counter, monotonic, time, process_time

# print("This is the time() output: {}".format(time()))
# print("This is the time() output: {}".format(monotonic()))
# print("This is the process_time() output: ".format(process_time()))
# print("This is the monotonic() output: {}".format(monotonic()))

import time


print("This is the time() output: {}".format(time.get_clock_info('time')))
print("This is the perf_counter() output: {}".format(time.get_clock_info('perf_counter')))
print("This is the process_time() output:")
print(time.get_clock_info('process_time'))
print("This is the monotonic() output: {}".format(time.get_clock_info('monotonic')))