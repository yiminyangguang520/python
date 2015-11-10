# encoding: utf-8
__author__ = 'ypw'
import os

# 处理文件名迁移乱码，原文件名：QQ#U622a#U56fe20150218111839.png
for root, dirnames, filenames in os.walk("."):
    try:
        for filename in filenames:
            print filename
            if filename.find("#U") != -1:
                filename2 = os.path.join(root, filename)
                filename3 = eval("u'" + filename.replace('#U', '\u') + "'")
                filename3 = os.path.join(root, filename3)
                os.rename(filename2, filename3)
                print filename2, filename3
    except Exception as ex:
        print ex.message
