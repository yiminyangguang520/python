# coding:utf-8
__author__ = 'yangpeiwen'

import socket
import urllib2
import os
from newscrawer2 import *
import threading
import Queue
import time

socket.setdefaulttimeout(10)
url = "http://xueqiu.com/statuses/stock_timeline.json?symbol_id=EDU&count=100&page="
q = Queue.Queue()


class DownloadThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get()
            link, path, title, newstime = task
            # print "得到任务:", title, "----", link, "time:", newstime
            try:
                content = getnewscontent(link)
                if len(content) > 5:
                    f = open(path, "w")
                    f.write(title + "\n\n")
                    f.write(link + "\n\n")
                    f.write(content.encode('utf-8', 'ignore'))
                    f.close()
                    print "完成任务:", title, "----", link, "time:", newstime
            except IOError as e:
                if str(e).find("time out") != -1:
                    task = (link, path, title, newstime)
                    q.put(task)
                    print "下载失败:", e, "重新下载", link
                else:
                    print "下载失败:错误信息:", e, link
            except Exception as e:
                print "下载失败:错误信息:", e, link
            time.sleep(0.1)
            if self.queue.empty():
                break


def downloadxueqiu(page):
    iurl = url + str(page)
    req = urllib2.Request(iurl)  # 创建一个urllib2里面的Request,这个request可以伪造HTTP头
    addheader(req, iurl)
    html = urllib2.urlopen(req).read()
    html = html.replace("false", "False")
    html = html.replace("true", "True")
    html = html.replace("null", "None")
    # 将javascript的false等,转为python的False
    urls = ""
    hosts = {}
    exec ("urls = " + html)  # 开挂直接把文本转成python里的变量
    ilists = urls['list']  # 文章都在list里面
    for ilist in ilists:
        if ilist['title']:  # title可能为None
            title = ilist['title']
            link = zhongjian(ilist['text'].decode('utf-8'), '>', '<')  # 寻找链接
            newstime = ilist['created_at']
            # print title, "----", link, "time:", time
            try:
                hosts[zhongjian(link.decode('utf-8'), "http://", "/")] = 1
            except:
                continue
            path = "news/" + str(newstime) + ".txt"
            if not os.path.exists(path):
                task = (link, path, title, newstime)
                q.put(task)
    print "获取列表完成", iurl, " queue:", q.qsize()


for i in range(1, 2):
    downloadxueqiu(i)

for i in range(10):
    t = DownloadThread(queue=q)
    t.start()
