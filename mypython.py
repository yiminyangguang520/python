# coding: utf-8
__author__ = 'node'
from math import *


# 1 1 2 3 5 8 13 ...

# a = 1
# b = 1
# for i in range(100):
# c = a+b
# a = b
# b = c
#     print c

# a = [1, 3, 7, 10, 4, 5, 67, 3]
# amax = a[0]
# for i in a:
#     if amax < i:
#         amax = i
# print amax

# a = input()
# b = input()
# c = input()
# delta = b*b-4*a*c
# if delta >= 0:
#     x1 = (math.sqrt(delta)-b)/(2*a)
#     x2 = (-math.sqrt(delta)-b)/(2*a)
#     print x1, x2
# else:
#     print '无解'

# a = [1, 3, 7, 10, 4, 5, 67, 3]
# b = len(a)
# print b
# for i in range(b):
#     print a[b-i-1],


# a = 100000
# b = 1
# for i in range(1, a+1, 1):
#     b *= i
# print b
#
# print "总用时:", time.time()-start

# a = 3
# i = 0
# print 2
# asd = 10
# while True:
#     c = sqrt(a)
#     k = 1
#     for j in range(2, int(c)+1, 1):
#         if a % j == 0:
#             k = 0
#     if k == 1:
#         i += 1
#         print a
#     a += 1
#     if i == 10:
#         break

# a = [1, 3, 7, 10, 4, 5, 67, 3]
# a.sort()
# print(a)

# b = len(a)
# c = []
# for i in range(b):
#     for j in range(0, b-1, 1):
#         if a[j] > a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp
# print a,


class node:
    def __init__(self, _data):
        self.data = _data
        self.next = None

first = node(1)
last = first
for i in range(4):
    temp = node(i+2)
    last.next = temp
    last = temp
last.next = first

temp = first
i = 1
while True:
    print temp.data
    if temp.next == temp:
        break
    else:
        if i % 3 == 0:
            print "删除了", temp.data
            last.next = temp.next
        last = temp
        temp = temp.next
    i += 1
print temp.data