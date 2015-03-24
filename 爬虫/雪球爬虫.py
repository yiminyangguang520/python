# coding:utf-8
__author__ = 'yangpeiwen'

import socket
import urllib2
import os
from newscrawer import *

socket.setdefaulttimeout(30)
url = "http://xueqiu.com/statuses/stock_timeline.json?symbol_id=MON&count=200&page=3"


def downloadxueqiu():
    req = urllib2.Request(url)  # 创建一个urllib2里面的Request,这个request可以伪造HTTP头
    addheader(req, url)
    html = urllib2.urlopen(req).read()
    html = html.replace("false", "False")
    html = html.replace("true", "True")
    html = html.replace("null", "None")
    # 将javascript的false等,转为python的False
    urls = ""
    hosts = {}
    exec("urls = " + html)  # 开挂直接把文本转成python里的变量
    ilists = urls['list']  # 文章都在list里面
    for ilist in ilists:
        if ilist['title']:  # title可能为None
            title = ilist['title']
            link = zhongjian(ilist['text'].decode('utf-8'), '>', '<')  # 寻找链接
            time = ilist['created_at']
            # print title, "----", link, "time:", time
            try:
                hosts[zhongjian(link.decode('utf-8'), "http://", "/")] = 1
            except:
                continue
            path = "news/" + str(time) + ".txt"
            if not os.path.exists(path):
                try:
                    content = getnewscontent(link)
                    if len(content) > 5:
                        f = open(path, "w")
                        f.write(title + "\n\n")
                        f.write(link + "\n\n")
                        f.write(content.encode('utf-8'))
                        f.close()
                        print title, "----", link, "time:", time
                except Exception as e:
                    print "下载失败:错误信息:", e
downloadxueqiu()