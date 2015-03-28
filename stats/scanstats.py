# coding:utf-8
__author__ = 'yangpeiwen'
from urllib import *
from bs4 import BeautifulSoup
import socket

socket.setdefaulttimeout(3)


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition)
    return yourstr[leftposition + len(leftstr):rightposition]


def lefturl(inurl):
    return inurl[0: inurl.rfind("/") + 1]


url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html'


def getlink(inurl):
    inhtml = urlopen(inurl).read()
    insoup = BeautifulSoup(inhtml)
    inall = insoup.findAll('a')
    inlinks = []
    for ina in inall:
        if ina['href'].find("html") != -1:
            inlinks += zip([(lefturl(inurl) + ina['href'])], [ina.text])
    return inlinks


try:
    links = getlink(url)
    for link, name in links:
        print link, name
        links2 = getlink(link)
        for link2, name2 in links2:
            print link2, name2
        break
except IOError:
    print '超时'