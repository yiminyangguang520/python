# coding: utf-8
__author__ = 'ypw'

import requests
from bs4 import BeautifulSoup
import threading
import os

all_course = 'https://teamtreehouse.com/tracks'
course_name = 'css-basics'
base = 'http://teamtreehouse.com'

s = requests.session()
s.headers[
    "Cookie"] = '_treehouse_session=ODdRN05SQXQwVC9EVjB2VHoxR0MwK2VpZUtQaFRFMXVQTHpEVUpNdVRWS0ZxWUJXR05kcFo4SHZvaElvRWRkZnJUZ3hkVlJOeWh2bGlmR0ZFZkRleVc3RkxTUFpRcnJnNnR5OTd3RmNKSzJqVkRmeUIyeUtWcytHdmltL3owenZZb1Q3L1lLSTB5Wk93c041Q2NCcUlIaEQ5RE1OS09lU3JCN0EwbktMNmh4WjdTWCtRVFdrRlcwOFRUY2c0U0lvR2w3R3Z3c0RDQ1JRek9GZFI4NGlobTBPK2d5RVpZVG9yeDNEclRCamRhcXA3b1ZnMEJ2KzRKQlBsWnJlMHlEZGYwazAzVU10M0VibnBXNU9KWUNqTUE0YmhLbkNSc3pjdkpyVS9idnRSSEhkZVlDOHQ3QnNHQlZFbHVRRmdTOHE3UGZXd1FhNTMzVmxIRVBxeUdKemw0TmhQd3MrTnhVWVBkdzJvU3l5dnJvQVI2RTBzL1I5NzJxbjh6dk5WQlRsWmtoNHQrOUlpOGFQUEUwVmZ4YmNYMExQUkY5SzVtRFhvMnBXcm5KQVNyUTVVUzVLY0FETDduVHVaQ2JyUWY4L0dmQ29mTkxNRjE0MDk3clJQT3RIaXc9PS0tNkpqcGoxSjMwSlBtVzNDWGNxT3ZTZz09--9f9072edd241e58f3bfd92007c6f1d4f261e0d7b; path=/; HttpOnly'
s.headers[
    "User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'

http_agent = 'http://915505626@qq.com:aaaaaa@hk2.nhpass.com:110'
proxies = {'http': http_agent, 'https': http_agent}

print "Start"
if not os.path.exists(course_name):
    os.makedirs(course_name)


def zhongjian(yourstr, leftstr, rightstr):
    leftposition = \
        yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition + len(leftstr))
    return yourstr[leftposition + len(leftstr):rightposition]
    # 取文本中间内容


urls = open(course_name + '/' + "urls.csv", "w")

getFilename = lambda inurl: inurl[inurl.rfind('/') + 1:]


def downloadFile(inurl, infilename):
    if not infilename:
        infilename = getFilename(inurl)
    inr = requests.get(inurl, proxies=proxies, stream=True)
    if os.path.isfile(course_name + '/' + infilename) is True:
        insize = os.path.getsize(course_name + '/' + infilename)
        if inr.headers.get('content-length'):
            if int(inr.headers['content-length']) - insize > 0:
                print "文件下载不全", infilename, int(inr.headers['content-length']) - insize
            else:
                return
    with open(course_name + '/' + infilename, "wb") as f:
        for chunk in inr.iter_content(chunk_size=1024 * 128):
            if chunk:
                f.write(chunk)
                f.flush()


class DownloadThread(threading.Thread):
    def __init__(self, iurl, iname):
        threading.Thread.__init__(self)
        self.url = iurl
        self.name = iname

    def run(self):
        self.r = s.get(self.url, proxies=proxies)
        self.soup = BeautifulSoup(self.r.text, "html.parser")
        for subtitleurl in self.soup.findAll(attrs={'kind': 'subtitles'}):
            if str(subtitleurl).find("2862") != -1:
                continue
            self.subtitleurl = subtitleurl
        try:
            self.subtitleurl = base + self.subtitleurl['src']
        except:
            print "非视频", self.url
            return
        self.download = self.soup.find(attrs={'title': 'Download'})
        self.downloadurl = None
        if self.download:
            if self.download.has_attr('href'):
                self.downloadurl = self.download['href']
        for source in self.soup.findAll(attrs={'type': 'video/mp4'}):
            self.videourl = source['src']
            self.filename = self.videourl[self.videourl.rfind("/") + 1:self.videourl.rfind('?')]
            if self.videourl.find('AskAQuestion') == -1:
                print "开始下载", self.videourl, self.filename, self.subtitleurl, self.downloadurl
                urls.write(
                    self.name + '.' + self.filename + ',' + self.videourl + ',' + self.subtitleurl + ',' + '\n')
                urls.flush()
                downloadFile(self.subtitleurl, self.name + '.' + self.filename.replace('mp4', 'srt'))
                if self.downloadurl:
                    downloadFile(self.downloadurl, None)
                downloadFile(self.videourl, self.name + '.' + self.filename)


r = s.get('http://teamtreehouse.com/library/' + course_name + '/', proxies=proxies)
soup = BeautifulSoup(r.text, "html.parser")

num = 0
for step in soup.findAll(attrs={'class': 'achievement-steps'}):
    for li in step.findAll('li'):
        a = li.find('a')
        title = li.find('strong')
        if a.has_attr('href') and str(a).find(course_name) > 0:
            print title.text, base + a['href']
            num += 1
            t = DownloadThread(base + a['href'], str(num) + '.' + title.text.replace('/', ''))
            t.start()
