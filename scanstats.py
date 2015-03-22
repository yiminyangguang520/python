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
        inlinks += zip([(lefturl(inurl)+ina['href'])], [ina.text])
    return inlinks

try:
    links = getlink(url)
    for link, name in links:
        print link, name
except IOError:
    print '超时'