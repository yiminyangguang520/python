# coding:utf-8
__author__ = 'yangpeiwen'

from urllib import *
from bs4 import BeautifulSoup
import socket
import os

url = "http://free.qidian.com/Free/ReadChapter.aspx?bookId=22881&chapterId=573116"
socket.setdefaulttimeout(3)
path = "xs"

socket.setdefaulttimeout(3)  # 3秒超时
if os.path.exists(path) is False:
    os.makedirs(path)
    # 如果没有这个文件夹就创建一个
f = open(path+"/xs.txt", "w")

always = True
while always:
    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        text = soup.find(attrs={'id': 'content'})
        texturl = text.find(charset='GB2312')['src']
        text = urlopen(texturl).read().decode('GBK')
        print text
        f.write(text.encode("utf-8"))
        if soup.find(attrs={'class': 'next'}).text.encode('utf-8').index('下一章') == 0:
            url = "http://free.qidian.com/" + soup.find(attrs={'class': 'next'})['href']
            print url
        else:
            break
    except IOError:
        print "error"
f.close()