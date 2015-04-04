# coding:utf-8
__author__ = 'yangpeiwen'

from urllib import *
from bs4 import BeautifulSoup
import socket
import os

url = "http://wap.jdxs.net/index.php/book/chapter/bid=100722/cid=20591139/"
path = "xs"

if os.path.exists(path + "/nowurl.txt"):
    nowurl = open(path + "/nowurl.txt", "r")
    url = nowurl.read()
    nowurl.close()
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    nexturl = "http://wap.jdxs.net/" + soup.find(id="btnNext")["href"]
    if (len(nexturl) > 0) & (nexturl != "http://wap.jdxs.net/index.php/book/cover/bid=100722/"):
        pass
    else:
        print "暂无最新章节"
        exit()
print url

socket.setdefaulttimeout(10)  # 3秒超时
if os.path.exists(path) is False:
    os.makedirs(path)
    # 如果没有这个文件夹就创建一个
f = open(path + "/y.txt", "a")


always = True
errortime = 0
while always:
    if errortime > 10:
        break
    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        chapter = soup.find(attrs={"class": "chapter"})
        print chapter.text
        f.write(chapter.text.encode('utf-8'))
        f.flush()
        nexturl = "http://wap.jdxs.net/" + soup.find(id="btnNext")["href"]
        if (len(nexturl) > 0) & (nexturl != "http://wap.jdxs.net/index.php/book/cover/bid=100722/"):
            url = nexturl
            nowurl = open(path + "/nowurl.txt", "w")
            nowurl.write(nexturl)
            nowurl.close()
        else:
            print "下载完毕"
            break
    except Exception as ex:
        errortime += 1
        print ex
        print "error"
f.close()