# # Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if i % 11 == 0 and i > 0:
#         break
#
# for i in range(1,21):
#     if i % 3 == 0 and i > 0:
#         continue
#     if i % 5 == 0 and i > 0:
#         continue
#     print(i)

for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
