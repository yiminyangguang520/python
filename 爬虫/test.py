# coding:utf-8
__author__ = 'yangpeiwen'
from newscrawer import *

content = getnewscontent("http://finance.sina.com.cn/stock/t/20150311/095421695136.shtml")
print content

# print urllib.urlopen("http://finance.sina.com.cn/stock/t/20150311/095421695136.shtml").read()