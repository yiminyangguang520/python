# coding:utf-8
__author__ = 'yangpeiwen'

import urllib
from bs4 import BeautifulSoup

attrContent = {"finance.sina.com.cn": {"id": "artibody"},
               "tech.sina.com.cn": {"id": "artibody"},
               "stock.sohu.com": {"itemprop": "articleBody"},
               "it.sohu.com": {"itemprop": "articleBody"},
               "finance.qq.com": {"id": "Cnt-Main-Article-QQ"},
               "tech.qq.com": {"id": "Cnt-Main-Article-QQ"},
               "jigou.21cbh.com": {"id": "Article"},
               "biz.21cbh.com": {"id": "Article"},
               "china.caixin.com": {"class": "text"},
               "magazine.caixin.com": {"class": "text"},
               "www.gw.com.cn": {"class": "inner"},
               "news.cnstock.com": {"id": "qmt_content_div"},
               "www.yicai.com": {"class": "text tline"},
               "www.ccin.com.cn": {"class": "con"},
               "stock.10jqka.com.cn": {"class": "art_main"},
               "info.glinfo.com": {"id": "text"},
               "stock.stockstar.com": {"class": "article"},
               "www.cpcia.org.cn": {"class": "content"},
               "industry.caijing.com.cn": {"id": "the_content"},
               "stock.caijing.com.cn": {"id": "the_content"},
               "money.163.com": {"id": "endText"},
               "www.p5w.net": {"class": "text"},
               "laoyaoba.com": {"id": "article_body"},
               "www.eeo.com.cn": {"id": "text_content"},
               "news.stcn.com": {"id": "ctrlfscont"},
               "news.imeigu.com": {"id": "endText"},
               }

attrContent2 = {"www.ccin.com.cn": {"class": "art_con"}}

nop = "stock.sohu.com,www.ccin.com.cn"


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition + len(leftstr))
    return yourstr[leftposition + len(leftstr):rightposition]
    # 取文本中间内容


def ifrefresh(ihtml):
    lowhtml = ihtml.lower()
    soup = BeautifulSoup(lowhtml)
    irefresh = soup.find(attrs={"http-equiv": "refresh"})
    if irefresh is not None:
        newurl = zhongjian(str(irefresh), "url=", '"')
        ihtml = urllib.urlopen(newurl).read()
    return ihtml


def getnewscontent(url):
    host = zhongjian(url, "http://", "/")
    if host in attrContent.keys():  # 如果host在列表中存在
        html = urllib.urlopen(url).read()
        html = htmldecode(html)
        html = ifrefresh(html)
    else:
        print "这个网址没有被收录:", url, host
        return ""
    soup = BeautifulSoup(html)
    if nop.find(host) != -1:    # 判断是否有p标签
        content = soup.find(attrs=attrContent[host])
        if content is None:
            if host in attrContent2.keys():  # 如果没找到就去列表2找
                content = soup.find(attrs=attrContent2[host])
                if content is not None:
                    content = content.text
                else:
                    content = ""
            else:
                content = ""
        else:
            content = content.text
    elif host in attrContent.keys():  # 如果host在列表中存在
        content = soup.find(attrs=attrContent[host])
        if content is None:
            if host in attrContent2.keys():  # 如果没找到就去列表2找
                content = soup.find(attrs=attrContent2[host]).text
            else:
                return ""
        else:
            content = content.text
        ps = content.findAll("p")
        content = ""
        for p in ps:
            content += p.text + "\n"
        content = content.replace("\n\n", "\n")
    return content