__author__ = 'yangpeiwen'

import os
from PIL import Image

for parent, dirnames, filenames in os.walk("/Users/yangpeiwen/Desktop/img/"):
    for filename in filenames:
        if filename.find(".jpg") != -1:
            im = Image.open("/Users/yangpeiwen/Desktop/img/" + filename)
            if im.size != (1920, 1080):
                print im.size, filename
