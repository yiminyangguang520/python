# coding:utf-8
__author__ = 'yangpeiwen'
from urllib import *
from bs4 import BeautifulSoup

url = "http://ypw.hk/macbook-no-hot/"


def getfilename(myurl):
    return myurl[myurl.rindex('/')+1:]
    # http://ypw.hk/wp-content/uploads/2015/03/QQ截图20150304174140.png
    # QQ截图20150304174140.png

html = urlopen(url).read()
soup = BeautifulSoup(html)
recent = soup.find(attrs={'class': 'entry-content'})
print(recent.text)
imgs = recent.findAll("img")
for img in imgs:
    url2 = img['src']
    print url2.encode('utf-8'), getfilename(url2)
    urlretrieve(url2.encode('utf-8'), getfilename(url2))