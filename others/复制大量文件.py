__author__ = 'Administrator'

import os
import shutil

for parent, dirnames, filenames in os.walk("n:/"):
    for filename in filenames:
        if filename.find("jpg") != -1:
            # print filename
            if not os.path.exists("k:/img/" + filename):
                print filename
                shutil.copyfile("n:/" + filename, "k:/img/" + filename)