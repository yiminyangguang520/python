# coding: utf-8
__author__ = 'ypw'

import time
import requests

yes = False
i = 0
s = requests.session()
url = "http://10.0.40.216/bgsxk/xk/LoginToXk"
postdata = {"USERNAME": "xuehao", "PASSWORD": "mima"}
r = s.post(url, params=postdata)
s.get("http://10.0.40.216/bgsxk/xk/getXkInfo?jx0502zbid=97&jx0502id=50")
# 历史类,其他类请自行抓包

def shua(inurl):
    global yes, i
    r2 = s.get(inurl, timeout=5)
    # 西方音乐史,其他课请自行抓包
    rec = r2.text
    i += 1
    print rec, i
    if rec.find("flag\":true") > 0:
        yes = True
    time.sleep(0.05)


while True:
    try:
        shua("http://10.0.40.216/bgsxk/xk/processXk?jx0502id=50&jx0404id=201520161002740&jx0502zbid=97")
        shua("http://10.0.40.216/bgsxk/xk/processXk?jx0502id=50&jx0404id=201520161002775&jx0502zbid=97")
        if yes:
            break
    except:
        pass

