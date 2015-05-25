# coding: utf-8
__author__ = 'Administrator'

import os
import shutil
import hashlib

from_ = "/Volumes/H/小米2S/"
to_ = "/Volumes/H/小米2S重复/"

sha1list = {}


def getsha1(_filename):
    h = hashlib.sha1()
    f = open(_filename)
    h.update(f.read())
    return h.hexdigest()


if __name__ == '__main__':
    for root, dirnames, filenames in os.walk(from_):
        try:
            for filename in filenames:
                filename2 = os.path.join(root, filename)
                sha1 = getsha1(filename2)
                if sha1 in sha1list:
                    shutil.move(filename2, to_ + filename)
                    print "发现重复文件:", filename2, sha1
                    break
                else:
                    sha1list[sha1] = 1
                    print "文件:", filename2, sha1
        except Exception as ex:
            print ex.message