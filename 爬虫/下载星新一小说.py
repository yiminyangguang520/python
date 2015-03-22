# coding: utf-8
__author__ = 'ypw'
 
from urllib import *
from progressbar import *
from bs4 import BeautifulSoup
import socket
import os
 
url = "http://www.xiexingcun.com/Global/xingxinyi/1.htm"  # 星新一小说
path = "x"

socket.setdefaulttimeout(3)  # 3秒超时
if os.path.exists(path) is False:
    os.makedirs(path)
    # 如果没有这个文件夹就创建一个
html = urlopen(url).read()
soup = BeautifulSoup(html)
# <a href="mydoc001.htm" target="_parent">被窃的文件</a> 寻找这样的链接
links = soup.find_all('a', target="_parent")
index = 0
pbar = ProgressBar(widgets=[Percentage(), Bar(), ETA()], maxval=len(links)).start()
# 建立一个进度条,ETA()是estimated time of arrival,剩余时间
for link in links:
    index += 1
    html2 = html = urlopen("http://www.xiexingcun.com/Global/xingxinyi/" + link['href']).read()
    soup2 = BeautifulSoup(html2)
    title = soup2.find("font", size="4").get_text()
    text = soup2.find("font", size="2").get_text()
    f = open(path+"/" + title + ".txt", "w")
    f.write(text.encode("utf-8"))
    f.close()
    pbar.update(index)
    # 更新进度条
pbar.finish()
