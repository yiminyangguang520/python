# coding: utf-8
__author__ = 'ypw'

from urllib import *
from bs4 import BeautifulSoup
import socket


socket.setdefaulttimeout(3)

f = open('data.csv', 'w')
r = "?date=2015-1-1"
t = 0
while True:
    t += 1
    html = urlopen("http://m.lssdjt.com/"+r).read()
    soup = BeautifulSoup(html)
    r = soup.find("li", "r")['onclick'].split("'")[1]
    for link in soup.find_all('a'):
        if link.string is not None:
            title = link.get_text()
            print title
            title = title.encode("gbk", "ignore")
            href = link['href']
            if href.find("html") > 0:
                success = True
                while success:
                    try:
                        print "getting " + href
                        urlretrieve("http://m.lssdjt.com/" + href, href)
                        success = False
                    except IOError:
                        print "超时"

            f.write(href + "," + title + "\n")
    print "这是第{0}天".format(t)
    if t > 365:
        break

f.close()
