# coding:utf-8
__author__ = 'yangpeiwen'

chrome_header = """
Host: xueqiu.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
cache-control: no-cache
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36 QQBrowser/3.0.2613.400
Accept-Encoding: deflate,sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: xq_a_token=9863acf1874182f3de6ea80874b21b2f0d568cd2; xq_r_token=35e0f3cd17d111a2d21f0aa9f857788ba4ee2cc5; __utmt=1; __utma=1.2130960166.1429345119.1429345119.1429345119.1; __utmb=1.1.10.1429345119; __utmc=1; __utmz=1.1429345119.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
"""


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition + len(leftstr))
    return yourstr[leftposition + len(leftstr):rightposition]
    # 取文本中间内容


def addheader(irequest, iurl, header=chrome_header):
    iheaders = header.split("\n")
    for iheader1 in iheaders:
        iheader2 = iheader1.split(":")
        try:
            irequest.add_header(iheader2[0], iheader2[1])
        except:
            pass
    irequest.add_header("Host", zhongjian(iurl, "//", "/"))
    print zhongjian(iurl, "//", "/")
# 添加Header防止网站反爬虫