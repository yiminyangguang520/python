__author__ = 'yangpeiwen'

from bs4 import BeautifulSoup
from urllib import *
import os
import socket

url = "http://192.168.191.2/img/"
socket.setdefaulttimeout(300)
html = urlopen(url).read()
soup = BeautifulSoup(html)
imgs = soup.findAll("img")
for img in imgs:
    print img['src']
    url2 = url + img['src']
    filepath = "/Volumes/YPW-M-1/img/" + img['src']
    if not os.path.exists(filepath):
        urlretrieve(url2.encode('utf-8'), filepath)
