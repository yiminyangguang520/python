# coding:utf-8
__author__ = 'yangpeiwen'
import requests


s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0',
                  'Cookie': 'xq_a_token=7fd433866f17942022661a942c06f2b5fe387c88; xq_r_token=b9d8e84b0e62e82d36dd90fb42ce5603fa154901; __utmt=1; __utma=1.1794468395.1427682478.1427682478.1427682478.1; __utmb=1.1.10.1427682478; __utmc=1; __utmz=1.1427682478.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1427682482; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1427682482'})
print s.headers
url = "http://xueqiu.com/statuses/stock_timeline.json?symbol_id=EDU&count=20&page="
r = s.get(url)
print r.text
