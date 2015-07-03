__author__ = 'ypw'

import time
import requests
s = requests.session()
url = "http://10.0.40.216/bgsxk/xk/LoginToXk"
postdata = {"USERNAME": "你的学号", "PASSWORD": "你的密码"}
r = s.post(url, params=postdata)
s.get("http://10.0.40.216/bgsxk/xk/getXkInfo?jx0502zbid=97&jx0502id=50")
# 历史类,其他类请自行抓包
i = 0
while True:
    try:
        r2 = s.get("http://10.0.40.216/bgsxk/xk/processXk?jx0502id=50&jx0404id=201520161002095&jx0502zbid=97", timeout=5)
        # 西方音乐史,其他课请自行抓包
        rec = r2.text
        print rec, i
        if rec.find("flag\":true") > 0:
            break
        time.sleep(0.05)
        i += 1
    except:
        pass
