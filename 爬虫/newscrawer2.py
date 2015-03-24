# coding:utf-8
__author__ = 'yangpeiwen'

import urllib
from ypw import *
from bs4 import BeautifulSoup
import chardet

attrContent = [{"id": "artibody"},
               {"id": "qmt_content_div"},
               {"id": "text"},
               {"id": "the_content"},
               {"id": "endText"},
               {"id": "article_body"},
               {"id": "text_content"},
               {"id": "ctrlfscont"},
               {"id": "Cnt-Main-Article-QQ"},
               {"id": "Article"},
               {"id": "bodytext"},
               {"id": "article_content"},
               {"itemprop": "articleBody"},
               {"class": "text"},
               {"class": "inner"},
               {"class": "text tline"},
               {"class": "text"},
               {"class": "con"},
               {"class": "art_main"},
               {"class": "article"},
               {"class": "content"},
               {"class": "art_content"},
]


def ifrefresh(ihtml):
    lowhtml = ihtml.lower()
    soup = BeautifulSoup(lowhtml)
    irefresh = soup.find(attrs={"http-equiv": "refresh"})
    if irefresh is not None:
        newurl = zhongjian(str(irefresh), "url=", '"')
        ihtml = urllib.urlopen(newurl).read()
    return ihtml


def htmldecode(ihtml):
    chardit1 = chardet.detect(ihtml)
    return ihtml.decode(chardit1['encoding'], "ignore")


def getnewscontent(url):
    html = urllib.urlopen(url).read()
    html = htmldecode(html)
    html = ifrefresh(html)
    soup = BeautifulSoup(html)
    for attr in attrContent:
        content = soup.find(attrs=attr)
        if content is None:
            continue
        else:
            ps = content.findAll("p")
            if ps is not None:
                for p in ps:
                    content = ""
                    content += p.text + "\n"
                    content = content.replace("\n\n", "\n")
            else:
                content = content.text
            break
    if content is None:
        print "没有找到内容", url
        content = ""
    return content