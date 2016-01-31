# encoding: utf-8
__author__ = 'ypw'

import os
import hashlib

from_ = "/Volumes/YPW/"
filedict = {}

for root, dirnames, filenames in os.walk(from_):
    for filename in filenames:
        filepath = root + filename
        filesize = os.path.getsize(filepath)
        filetime = os.path.getmtime(filepath)
        if filetime > 1451600000:
            os.remove(filepath)
            print "file error:", filepath, ",filesize:", filesize
            continue
        with open(filepath, 'rb') as f:
            sha1obj = hashlib.sha1()
            sha1obj.update(f.read())
            hashvalue = sha1obj.hexdigest()
            if hashvalue in filedict:
                print "file exist:", filepath, ",filesize:", filesize
                os.remove(filepath)
            else:
                filedict[hashvalue] = filepath

