# coding:utf-8
__author__ = 'Administrator'

from urllib import *
from bs4 import BeautifulSoup
import socket

url = 'http://libopac.btbu.edu.cn:8080/opac/browseByCategory?pager.offset='
socket.setdefaulttimeout(3)  # 3秒超时
maxnum = 634309
print "\n"

f = open('library2.txt', 'a')
offset = 192800
to = offset + 10000
# 续传
while offset < maxnum:
    # 目录
    try:
        html = urlopen(url + str(offset)).read().decode('utf-8')
        soup = BeautifulSoup(html)
        links = soup.findAll(target='_blank')
        writecontent = ""
        offset2 = 0
        for link in links:
            try:
                url2 = 'http://libopac.btbu.edu.cn:8080' + link['href']
                # print link.text, url2
                writecontent += url2.encode('utf-8', 'ignore') + "\n" + link.text.encode('utf-8', 'ignore') + "\n"
                # 标题信息和内容
                html2 = urlopen(url2).read()
                soup2 = BeautifulSoup(html2)
                writecontent += soup2.find(id='detailsTable').text.encode('utf-8', 'ignore') + "\n"
                # 获得馆藏信息    getHoldingsInformation
                json3 = urlopen(url2.replace('book', 'book/getHoldingsInformation')).read()
                writecontent += json3 + "\n\n"
                offset2 += 1
                print "\r" + str(offset)+"    "+str(offset + offset2) + "/" + str(maxnum) + "    " + str(
                    offset * 100.0 / maxnum) + "%   第" + str(offset / 25) + "页",
            except Exception:
                # 为了防止某些失效链接,我们将跳过失败的书籍
                # 比如http://libopac.btbu.edu.cn:8080/opac/book/627232
                pass
        offset += 25
        writecontent += "\n==========第" + str(offset / 25) + "页==========\n\n"
        print "\r" + str(offset) + "/" + str(maxnum) + "    " + str(offset * 100.0 / maxnum) + "%   第" + str(
            offset / 25) + "页",
        f.write(writecontent)
        f.flush()
    except IOError:
        # print 'timeout'
        pass
    except Exception, e:
        print e
f.close()