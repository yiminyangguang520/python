__author__ = 'yangpeiwen'

import time
import os


def getmon():
    f = open("mon.csv", "r")
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


mylist = getmon()
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
            if mylist[timestring] > 0:
                os.rename(filename, "zhang/" + filename)
            elif mylist[timestring] < 0:
                os.rename(filename, "die/" + filename)
            else:
                os.rename(filename, "none/" + filename)