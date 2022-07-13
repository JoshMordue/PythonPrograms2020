# jabber = open("D:\\new downloads\\sample.txt",'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')

# with open("D:\\new downloads\\sample.txt",'r') as jabber:
#
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("D:\\new downloads\\sample.txt",'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

with open("D:\\new downloads\\sample.txt",'r') as jabber:
    lines = jabber.readlines()

for line in lines:
     print(line, end='')