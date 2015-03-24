# coding:utf-8
__author__ = 'yangpeiwen'
from newscrawer2 import *

content = getnewscontent("http://www.techweb.com.cn/world/2015-03-24/2136365.shtml")
print content

# print urllib.urlopen("http://finance.sina.com.cn/stock/t/20150311/095421695136.shtml").read()