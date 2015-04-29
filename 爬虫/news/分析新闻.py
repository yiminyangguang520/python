# coding: utf-8
__author__ = 'yangpeiwen'

import jieba
import jieba.analyse
import os
import re

jieba.enable_parallel(4)
jieba.analyse.set_stop_words("stop_words.txt")
# jieba.analyse.set_idf_path("idf.txt")
path = "跌"


def fenxi():
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.find("txt") != -1:
                wb = open(path + "/" + filename).read()
                wb = re.sub(r'http.+', '', wb)
                tags = jieba.analyse.extract_tags(wb, topK=10)
                print(",".join(tags))
                # , withWeight=True
                # for tag in tags:
                #     print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
                #     break
                # break

if __name__ == '__main__':
    fenxi()