# coding: utf-8
# a = raw_input()
# for word in a.split(" "):
# print word[::-1],

# n = input()
# s = 0
# for i in range(n):
# number = input()
# s += number
# print s

# 全局变量使用
# name = 'lhy'


# def say_hello():
# print 'hello ' + name
#
# say_hello()

# def change_name(new_name):
# # global name
# name = new_name
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

# asd = "17812345678,18612345678"
# import re
# print "\n".join(re.findall(r"\d{11}", asd))

# import re
#
#
# class WordDictionary:
#     def __init__(self):
#         self.str = ""
#
#     # @param {string} word
#     # @return {void}
#     # Adds a word into the data structure.
#
#     def addWord(self, word):
#         self.str += word
#
#     # @param {string} word
#     # @return {boolean}
#     # Returns if the word is in the data structure. A word could
#     # contain the dot character '.' to represent any one letter.
#     def search(self, word):
#         if self.str.find(word) != -1:
#             return True
#         return len(re.findall(word, self.str)) != 0
#
# # Your WordDictionary object will be instantiated and called as such:
# # wordDictionary = WordDictionary()
# # wordDictionary.addWord("word")
# # wordDictionary.search("pattern")
#
# wd = WordDictionary()
# wd.addWord("bad")
# wd.addWord("dad")
# wd.addWord("mad")
# print wd.search("pad")  # -> false
# print wd.search("bad")  # -> true
# print wd.search(".ad")  # -> true
# print wd.search("b..")  # -> true

# from math import *
#
# print str(factorial(100))

# nums1 = [0]
# nums2 = [1]
# m = 0
# n = 1
#
# str1 = nums1[:m]
# str2 = nums2[:n]
# str3 = str1 + str2
# str3.sort()
# nums1 = str3
# print nums1

# asd = """
# ---
# 计费方式:包月(允许国际)[M1-T]L020 [C1]
# ---
# 每月免费定额(RMB):	      0.00元
# 当前剩余网费(RMB):	      8.72元
# 本月免费余额(RMB):	      0.00元
# ---
# 最低保证金(RMB):		      0.50元
# ---
# 开户日期:		    20130821
# 最后使用日期:		    20150527
# 本月剩余可用流量:	     20480兆字节
# 本月剩余免费流量:	      2560兆字节
# 其它认证用ID:		    D31304A4
#
# """
#
# import re
#
# results = re.findall(r"(\d+)兆", asd)
# liuliang = 0
# print results
# for tmp in results:
#     liuliang += int(tmp)
# print liuliang

import requests
from pylab import *

data = requests.get("http://pic3.zhimg.com/39420a7da_m.jpg")

imshow(data)
