# coding:utf-8
__author__ = 'yangpeiwen'
from newscrawer2 import *

content = getnewscontent("http://tech.sina.com.cn/i/2015-02-11/doc-icczmvun6020524.shtml")
print content, type(content)
# print urllib.urlopen("http://finance.sina.com.cn/chanjing/gsnews/20140718/183619752276.shtml").read()