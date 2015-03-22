# coding:utf-8
__author__ = 'yangpeiwen'

from urllib2 import *
import socket


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition)
    return yourstr[leftposition+len(leftstr):rightposition]
    # 取文本中间内容

header = """
Host: xueqiu.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
cache-control: no-cache
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36 QQBrowser/3.0.2613.400
Referer: http://xueqiu.com/S/MON
Accept-Encoding: deflate,sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: xq_a_token=f04765824325b4fdaf86c559e528bd4322a38873; xq_r_token=88deececc3852b877ed15dd7795761e9a6790ea7; __utmt=1; __utma=1.1891582346.1427038206.1427038206.1427038206.1; __utmb=1.1.10.1427038206; __utmc=1; __utmz=1.1427038206.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
"""


def addheader(irequest, iheader):
    iheaders = iheader.split("\n")
    for iheader1 in iheaders:
        iheader2 = iheader1.split(":")
        try:
            irequest.add_header(iheader2[0], iheader2[1])
        except:
            pass
# 添加Header防止网站反爬虫

asd = "http://xueqiu.com/statuses/stock_timeline.json?symbol_id=MON&count=200&page=1"
url = Request(asd)  # 创建一个urllib2里面的Request,这个request可以伪造HTTP头
addheader(url, header)
socket.setdefaulttimeout(10)

html = urlopen(url).read()
html = html.replace("false", "False")
html = html.replace("true", "True")
html = html.replace("null", "None")
# 将javascript的false等,转为python的False
print html
urls = ""
exec("urls = "+html)  # 开挂直接把文本转成python里的变量
ilists = urls['list']  # 文章都在list理=里面
for ilist in ilists:
    if ilist['title']:  # title可能为None
        link = zhongjian(ilist['text'].decode('utf-8'), '>', '<')  #寻找链接
        print ilist['title'], "----", link