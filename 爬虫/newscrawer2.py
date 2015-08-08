# coding:utf-8
__author__ = 'yangpeiwen'

import requests
from bs4 import BeautifulSoup

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

#
# def ifrefresh(ihtml):
#     lowhtml = ihtml.lower()
#     soup = BeautifulSoup(lowhtml)
#     irefresh = soup.find(attrs={"http-equiv": "refresh"})
#     if irefresh is not None:
#         newurl = zhongjian(str(irefresh), "url=", '"')
#         ihtml = urllib.urlopen(newurl).read()
#     return ihtml


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition + len(leftstr))
    return yourstr[leftposition + len(leftstr):rightposition]
    # 取文本中间内容


def getnewscontent(url):
    r = requests.get(url)
    # 以下是解决各种乱码问题
    if r.encoding == "ISO-8859-1":
        r.encoding = r.apparent_encoding

    html = r.text
    # html = ifrefresh(html)
    # , from_encoding='gb18030'
    soup = BeautifulSoup(html, from_encoding='gb18030')
    for attr in attrContent:
        content = soup.find(attrs=attr)
        if content is None:
            continue
        else:
            ps = content.findAll("p")
            if str(ps) != "[]":
                content = ""
                for p in ps:
                    content += p.text + "\n"
                content = content.replace("\n\n", "\n")
            else:
                content = str(content).replace("<br>", "\n")
                content = str(content).replace("<br/>", "\n")
                content = BeautifulSoup(content).text
            break
    if content is None:
        print("没有找到内容", url)
        content = ""

    return content
