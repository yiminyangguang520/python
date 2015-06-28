# coding: utf-8
from data import *

data = getData(ZHIJIAO)

# for x in range(WIDTH - 1):
#     for y in range(HEIGHT - 1):
#         if (data[y][x] == '1') & (data[y][x+1] == '0'):
#             data[y][x] = ' '
#         if (data[y][x] == '0') & (data[y][x+1] == '1'):
#             data[y][x] = ' '

white = []
try:
    for y in range(HEIGHT - 1):
        dot = 0
        for x in range(WIDTH - 1):
            if data[y][x] == '0':
                dot += 1
        white.append(dot)
        print dot
except:
    print x, y

print "微分"
lastwhite = 0
for i in white:
    print i - lastwhite
    lastwhite = i

printData2(data, 47)
