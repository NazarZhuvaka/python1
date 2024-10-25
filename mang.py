# file = open('111.txt', 'w', encoding='utf-8')
#
# file.close()

# lst = []

# for i in range(10000):
#     with open('111.txt', 'w', encoding='utf-8') as fileN:
#         fileN.write('1213')
#         lst.append(fileN)
#     # file.close()

# with open('111.txt', 'w', encoding='utf-8') as fileN:
#     fileN.write('1213')
#     fileN.write('qwweq')
# print(fileN)

import os

with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")
