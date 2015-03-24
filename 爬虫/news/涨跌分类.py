# coding: utf-8
__author__ = 'yangpeiwen'

import time
import os


if not os.path.exists("涨"):
    os.mkdir("涨")
if not os.path.exists("跌"):
    os.mkdir("跌")
if not os.path.exists("平"):
    os.mkdir("平")


def getcsvdata():
    f = open("EDU.csv", "r")
    f.readline()
    f.readline()
    ilist = {}

    try:
        while True:
            line = f.readline()
            asd = ""
            exec("asd = [" + line + "]")
            qwe = float(asd[1]) - float(asd[3])
            ilist[asd[0]] = qwe
    except:
        pass
    return ilist


mylist = getcsvdata()
for parent, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.find(".txt") != -1:
            timestamp = float(filename[:10])
            while True:
                timestamp += (3600 * 24)
                timearray = time.localtime(timestamp)
                timestring = time.strftime("%Y/%m/%d", timearray)
                if timestring in mylist.keys():
                    break
            print filename, timestring, mylist[timestring]
            try:
                if mylist[timestring] > 0:
                    os.rename(filename, "涨/" + filename)
                elif mylist[timestring] < 0:
                    os.rename(filename, "跌/" + filename)
                else:
                    os.rename(filename, "平/" + filename)
            except:
                pass