# coding:utf-8
__author__ = 'yangpeiwen'
import requests

r = requests.get("http://ypw.hk/images/logo.png")
print r.status_code
print r.headers['content-type']

from PIL import Image
from matplotlib.pyplot import *
from StringIO import StringIO
I = Image.open(StringIO(r.content))

imshow(I)
show()