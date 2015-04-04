# coding: utf-8
__author__ = 'Administrator'
import os

fileall = open("libraryall.txt", 'r')
fileall.seek(-10000, os.SEEK_END)
text = ""


def getfilename(myurl):
    return myurl[myurl.rindex('/')+1:]

lines = fileall.readlines()

i = 0
while True:
    while True:
        text = lines[i]
        if text.find("http://libopac.btbu.edu.cn") >= 0:
            break  # 循环找到起点,网址
        i += 1
        if i >= len(lines):
            break
    if i >= len(lines):
        break
    link = text.strip()
    bookid = getfilename(text).strip()
    i += 1
    name = lines[i].strip()  # 下一行是书名
    i += 1
    detail = ""
    while True:
        detail += lines[i]
        i += 1
        if len(lines[i]) <= 2:
            break
    detail = detail.strip()
    i += 1
    guancang = lines[i].strip()
    guancang = guancang.replace("false", "False")
    guancang = guancang.replace("true", "True")
    print link, bookid, name, detail, guancang
    try:
        exec("guancang = "+guancang)
        for item in guancang:
            print "-----------"
            for item2 in item:
                if (item2 == '索书号') | (item2 == '条形码') | (item2 == '部门名称') | (item2 == '备注'):
                    print item2, item[item2]
    except:
        pass
    print "\n"
    i += 1
