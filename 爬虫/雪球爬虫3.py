# coding: utf-8
__author__ = 'yangpeiwen'

import socket
import threading
import queue
import time
import requests
from bs4 import BeautifulSoup

socket.setdefaulttimeout(10)
url = "http://xueqiu.com/statuses/stock_timeline.json?symbol_id=EDU&count=100&page="
q = queue.Queue()

s = requests.session()
s.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
s.get("http://xueqiu.com")
# 反反爬虫策略：设置agent为普通浏览器，然后访问首页获取cookie

attrContent = [{"itemprop": "articleBody"},
               {"id": "Cnt-Main-Article-QQ"},
               {"id": "Main_Content_Val"},
               {"id": "artibody"},
               {"id": "arttext"},
               {"id": "main_content"},
               {"id": "articleContent"},
               {"id": "qmt_content_div"},
               {"id": "text"},
               {"id": "the_content"},
               {"id": "endText"},
               {"id": "article_body"},
               {"id": "text_content"},
               {"id": "ctrlfscont"},
               {"id": "Article"},
               {"id": "bodytext"},
               {"id": "article_content"},
               {"id": "newscontent"},
               {"id": "vcontent"},
               {"id": "Content"},
               {"class": "Index_ShowDetail_Content"},
               {"class": "textCon"},
               {"class": "articon"},
               {"class": "article"},
               {"class": "NewsBody"},
               {"class": "main_article"},
               {"class": "text"},
               {"class": "inner"},
               {"class": "text tline"},
               {"class": "text"},
               {"class": "con"},
               {"class": "ContA"},
               {"class": "art_main"},
               {"class": "content"},
               {"class": "art_content"},
               ]


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition + len(leftstr))
    return yourstr[leftposition + len(leftstr):rightposition]
    # 取文本中间内容


def getnewscontent(iurl):
    global icontent
    r = requests.get(iurl)
    # 以下是解决各种乱码问题
    if r.encoding == "ISO-8859-1":
        r.encoding = r.apparent_encoding
    html = r.text
    # html = ifrefresh(html)
    # , from_encoding='gb18030'
    soup = BeautifulSoup(html, from_encoding='gb18030')
    for attr in attrContent:
        icontent = soup.find(attrs=attr)
        if icontent is None:
            continue
        else:
            ps = icontent.findAll("p")
            if str(ps) != "[]":
                icontent = ""
                for p in ps:
                    icontent += p.text + "\n"
                icontent = icontent.replace("\n\n", "\n")
            else:
                icontent = str(icontent).replace("<br>", "\n")
                icontent = str(icontent).replace("<br/>", "\n")
                icontent = BeautifulSoup(icontent).text
            break
    if icontent is None:
        print("没有找到内容", url)
        icontent = ""

    return icontent


class DownloadThread(threading.Thread):
    # 这个线程用于在队列中寻找任务，然后下载新闻
    def __init__(self, iqueue):
        threading.Thread.__init__(self)
        self.queue = iqueue

    def run(self):
        while True:
            task = self.queue.get()
            link, path, title, newstime = task
            # print "得到任务:", title, "----", link, "time:", newstime
            try:
                self.content = getnewscontent(link)
                # print(self.content)
                if len(self.content) > 5:
                    f = open(path, "w", encoding="UTF-8")
                    f.write(title + "\n\n")
                    f.write(link + "\n\n")
                    f.write(self.content)
                    f.close()
                    print("完成任务:", title, "----", link, "time:", newstime)
            except IOError as e:
                if str(e).find("time out") != -1:
                    task = (link, path, title, newstime)
                    q.put(task)
                    print("下载失败:", e, "重新下载", link)
                else:
                    print("下载失败:错误信息:", e, link)
            except Exception as e:
                print("下载失败:错误信息:", e, link)
            time.sleep(0.1)
            if self.queue.empty():
                break


def downloadxueqiu(page):   # 获取股票的新闻链接
    iurl = url + str(page)
    urls = s.get(iurl).json()  # 创建一个urllib2里面的Request,这个request可以伪造HTTP头
    # pattern = """"title":"(.+?)","text":".+?>(http.+?)<.+?\""""
    ilists = urls['list']  # 文章都在list里面
    for ilist in ilists:
        if ilist['title']:  # title可能为None
            title = ilist['title']
            link = zhongjian(ilist['text'], '>', '<')  # 寻找链接
            newstime = ilist['created_at']
            # print title, "----", link, "time:", time
            path = "news/" + str(newstime) + ".txt"
            # if not os.path.exists(path):
            task = (link, path, title, newstime)
            print(task)
            q.put(task)
    print("获取列表完成", iurl, " queue:", q.qsize())


for i in range(1, 2):
    downloadxueqiu(i)

for i in range(10):
    t = DownloadThread(q)
    t.start()

# q.put(('http://it.sohu.com/20150802/n418016582.shtml', 'news/1438506294000.txt', '新东方加码智能化学习产品 推“知心系列”', 1438506294000))
# q.put(('http://people.techweb.com.cn/2015-07-18/2177277.shtml', 'news/1437195993000.txt', '俞敏洪：即使A股能让新东方市值翻10倍也不会回来', 1437195993000))
