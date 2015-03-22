__author__ = 'yangpeiwen'

from urllib import *
from bs4 import BeautifulSoup

url = "http://wap.jdxs.net/index.php/book/chapter/bid=100722/cid=20691965/"

html = urlopen(url).read()
soup = BeautifulSoup(html)
text = soup.find(attrs={'class': 'chapter'}).text
print text