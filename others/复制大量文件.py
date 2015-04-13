__author__ = 'Administrator'

import os
import shutil

from_ = "/Volumes/YPW/"
to_ = "/Volumes/YPW-M-1/img/"

for parent, dirnames, filenames in os.walk(from_):
    for filename in filenames:
        if filename.find("jpg") != -1:
            # print filename
            if not os.path.exists(to_ + filename):
                print filename
                shutil.copyfile(from_ + filename, to_ + filename)