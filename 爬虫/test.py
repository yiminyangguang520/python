import requests
from bs4 import BeautifulSoup

r = requests.get("http://club.mil.news.sina.com.cn/thread-666013-1-1.html")
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text)
result = soup.find(attrs={"class": "cont f14"})
print result.text
