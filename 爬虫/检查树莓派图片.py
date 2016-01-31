__author__ = 'yangpeiwen'

import os

for parent, dirnames, filenames in os.walk("/Users/yangpeiwen/Desktop/img/"):
    for filename in filenames:
        if filename.find(".jpg") != -1:
            f = open("/Users/yangpeiwen/Desktop/img/" + filename)
            f.seek(-1, 2)
            data = ord(f.read())
            if data != 217:
                os.remove("/Users/yangpeiwen/Desktop/img/" + filename)
                print filename
