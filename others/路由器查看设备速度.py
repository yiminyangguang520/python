# coding: utf-8
__author__ = 'ypw'

import urllib2
import socket
import time
import os

url = "http://192.168.0.1/"
urlspeed = "http://192.168.0.1/userRpm/SystemStatisticRpm.htm?contType=1&sortType=5&Num_per_page=50&Goto_page=1"
socket.setdefaulttimeout(3)
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'Authorization=Basic%20YWRtaW46MTIzNDU2;'))
request = urllib2.Request(urlspeed)
request.add_header("Referer", "http://192.168.0.1/userRpm/MenuRpm.htm")


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition)
    return yourstr[leftposition+len(leftstr):rightposition]


def tospd(string):
    string = int(string)
    if string > 1024*1024:
        return str(string/1024/1024)+"MB/s"
    elif string > 1024:
        return str(string/1024)+"KB/s"
    else:
        return str(string)+"B/s"

while True:
    html = opener.open(request).read()
    content = zhongjian(html, "Array(\n", ")")
    content1 = content.split("\n")
    os.system("cls")
    for content2 in content1:
        content3 = content2.split(",")
        if len(content3) >= 8:
            print content3[1], content3[2], tospd(content3[5]), tospd(content3[6])
    time.sleep(0.5)
