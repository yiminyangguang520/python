# coding: utf-8
# a = raw_input()
# for word in a.split(" "):
# print word[::-1],

# n = input()
# s = 0
# for i in range(n):
#     number = input()
#     s += number
# print s

# 全局变量使用
# name = 'lhy'


# def say_hello():
#     print 'hello ' + name
#
# say_hello()

# def change_name(new_name):
#     # global name
#     name = new_name
#     print name
# change_name('wbd')

# s = 'appleasd'
# a = ''
# for i in range(-1, -1 - len(s), -1):
#     a += s[i]
# print a
# print s[::-1]

# import urllib
# a = raw_input()
# print urllib.urlopen(a).read()

# try:
#     print open("a.txt").read()
# except Exception as e:
#     print e
# import os
# print os.path.split(os.path.realpath(__file__))[0]

asd = "17812345678,18612345678"
import re
print "\n".join(re.findall(r"\d{11}", asd))