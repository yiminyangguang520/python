# coding:utf-8
__author__ = 'Administrator'

from urllib import *
from bs4 import BeautifulSoup
import socket
import threading
import Queue
import time

url = 'http://libopac.btbu.edu.cn:8080/opac/browseByCategory?pager.offset='
socket.setdefaulttimeout(20)  # 3秒超时
maxnum = 634404  # 图书总数
print "\n"

q = Queue.Queue()  # 构造一个队列,它可以put入任务和get出任务,先进先出
# 比如放入1,2,3,4,5    则你取出来的时候也是取出来1,2,3,4,5这样的顺序
f = open('library5.txt', 'a')


def getlinks():
    # 线程1,获取链接的线程
    offset = 526325  # 调这个值可以断点续传
    while offset < maxnum:
        try:
            html = urlopen(url + str(offset)).read().decode('utf-8')
            soup = BeautifulSoup(html)
            links = soup.findAll(target='_blank')  # 寻找所有的链接
            onetask = (offset, links)  # 构建一个(offset, links)结构作为task,其实就是(下到第几本书了, 链接们是什么)
            q.put(onetask)  # 放入queue中
            offset += 25
            print "\r" + str(offset) + "/" + str(maxnum) + "    " + str(offset * 100.0 / maxnum) + "%   第" + str(
                offset / 25) + "页----获取列表",
        except IOError:
            # print 'timeout'
            pass
        except Exception, e:
            print e


class MyThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue  # 初始化构造函数,传入queue

    def run(self):
        while True:
            myonetask = self.queue.get()  # 获取任务
            myoffset, mylinks = myonetask  # 解析任务
            # print "\r" + str(myoffset) + "/" + str(maxnum) + "    " + str(myoffset * 100.0 / maxnum) + "%   第" \
            #       + str(myoffset / 25) + "页----收到任务"
            mywritecontent = ""
            for mylink in mylinks:
                always = True  # 建立一个循环下载,
                while always:
                    try:
                        myurl2 = 'http://libopac.btbu.edu.cn:8080' + mylink['href']
                        # print link.text, url2
                        mywritecontent += myurl2.encode('utf-8', 'ignore') + "\n"
                        mywritecontent += mylink.text.encode('utf-8', 'ignore') + "\n"
                        # 标题信息和内容
                        myhtml2 = urlopen(myurl2).read()
                        mysoup2 = BeautifulSoup(myhtml2)
                        mywritecontent += mysoup2.find(id='detailsTable').text.encode('utf-8', 'ignore') + "\n"
                        # 获得馆藏信息    getHoldingsInformation
                        myjson3 = urlopen(myurl2.replace('book', 'book/getHoldingsInformation')).read()
                        mywritecontent += myjson3 + "\n\n"
                        always = False  # 下载成功之后才取消循环
                    except IOError:
                        pass  # 如果是IOError就是超时了,pass掉(相当于C++的;空语句)
                    except Exception:
                        # 为了防止某些失效链接,我们将跳过失败的书籍
                        # 比如http://libopac.btbu.edu.cn:8080/opac/book/627232
                        always = False
            print "\r" + str(myoffset) + "/" + str(maxnum) + "    " + str(myoffset * 100.0 / maxnum) + "%   第" \
                  + str(myoffset / 25) + "页----下载完成----" + str(myoffset + 25)
            mywritecontent += "\n==========第" + str(myoffset / 25) + "页==========\n\n"
            f.write(mywritecontent)
            f.flush()  # 写出到文件
            time.sleep(0.01)  # 线程累了 休息一下


t1 = threading.Thread(target=getlinks)  # 获取链接的线程
t1.start()

for asd in range(10):
    t2 = MyThread(q)  # 从队列里下载数据的线程
    t2.start()