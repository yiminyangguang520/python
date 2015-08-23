# coding: utf-8
__author__ = 'ypw'

import requests
import os
import Queue
import threading
import socket
import time
from bs4 import BeautifulSoup

# setup
socket.setdefaulttimeout(60)
all_course = 'https://teamtreehouse.com/tracks'
course_name = 'build-a-simple-iphone-app-with-swift'
todir = '5.' + course_name
base = 'http://teamtreehouse.com'
q = Queue.Queue()
s = requests.session()
s.headers["Cookie"] = '_treehouse_session=ODdRN05SQXQwVC9EVjB2VHoxR0MwK2VpZUtQaFRFMXVQTHpEVUpNdVRWS0ZxWUJXR05kcFo4SHZvaElvRWRkZnJUZ3hkVlJOeWh2bGlmR0ZFZkRleVc3RkxTUFpRcnJnNnR5OTd3RmNKSzJqVkRmeUIyeUtWcytHdmltL3owenZZb1Q3L1lLSTB5Wk93c041Q2NCcUlIaEQ5RE1OS09lU3JCN0EwbktMNmh4WjdTWCtRVFdrRlcwOFRUY2c0U0lvR2w3R3Z3c0RDQ1JRek9GZFI4NGlobTBPK2d5RVpZVG9yeDNEclRCamRhcXA3b1ZnMEJ2KzRKQlBsWnJlMHlEZGYwazAzVU10M0VibnBXNU9KWUNqTUE0YmhLbkNSc3pjdkpyVS9idnRSSEhkZVlDOHQ3QnNHQlZFbHVRRmdTOHE3UGZXd1FhNTMzVmxIRVBxeUdKemw0TmhQd3MrTnhVWVBkdzJvU3l5dnJvQVI2RTBzL1I5NzJxbjh6dk5WQlRsWmtoNHQrOUlpOGFQUEUwVmZ4YmNYMExQUkY5SzVtRFhvMnBXcm5KQVNyUTVVUzVLY0FETDduVHVaQ2JyUWY4L0dmQ29mTkxNRjE0MDk3clJQT3RIaXc9PS0tNkpqcGoxSjMwSlBtVzNDWGNxT3ZTZz09--9f9072edd241e58f3bfd92007c6f1d4f261e0d7b; path=/; HttpOnly'
s.headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'

http_agent = 'http://915505626@qq.com:aaaaaa@hk2.nhpass.com:110'
proxies = {'http': http_agent, 'https': http_agent}
try:
    os.makedirs(todir)
except:
    pass
info = open(todir + '/info.csv', 'w')
getFilename = lambda inurl: inurl[inurl.rfind('/') + 1:]


def utf(instr):
    if not instr:
        return 'None'
    return instr.encode('utf-8', 'ignore')


def getsoup(inurl):
    try:
        insoup = BeautifulSoup(s.get(inurl, proxies=proxies).text, "html5lib")
    except:
        insoup = BeautifulSoup(s.get(inurl, proxies=proxies).text, "html5lib")
        pass
    return insoup


def downloadFile(inurl, indir, infilename):
    infilename = indir + infilename.replace('/', '')
    print "文件名", infilename
    inr = requests.get(inurl, proxies=proxies, stream=True)
    if os.path.isfile(infilename) is True:
        if infilename.find('srt') > 0:
            q.task_done()
            return
        if inr.headers.get('content-length'):
            insize = os.path.getsize(infilename)
            if int(inr.headers['content-length']) - insize > 0:
                print "文件下载不全", infilename, int(inr.headers['content-length']) - insize
            else:
                print "已下载", infilename
                q.task_done()
                return
    print '开始下载', infilename, inurl
    with open(infilename, "wb") as f:
        for chunk in inr.iter_content(chunk_size=1024 * 128):
            if chunk:
                f.write(chunk)
                f.flush()
    q.task_done()
    print '下载完成', infilename, "剩余任务:", q.unfinished_tasks, finish

finish = False
num = 0


class DownloadThread(threading.Thread):
    # 这个线程用于在队列中寻找任务，然后下载新闻
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global finish
        while q.unfinished_tasks != 0 or not finish:
            (url, indir, filename) = q.get()
            downloadFile(url, indir, filename)


def getchapter(iurl):
    soup = getsoup(iurl)
    global num
    for contained in soup.find_all(attrs={'data-featurette': 'expandable-content-card'}):
        steptitle = contained.find(attrs={'class': 'trigger-steps toggle-steps'}).text
        step = contained.find(attrs={'class': 'achievement-steps'})
        for li in step.find_all('li'):
            try:
                a = li.find('a')
                title = li.find('strong')
                print steptitle, title.text, base + a['href']
                num += 1
                getresources(base + a['href'], steptitle, str(num) + '.' + title.text)
            except:
                pass
    global finish
    finish = True


def getresources(iurl, isteptitle, ititle):
    soup = getsoup(iurl)
    subtitleurl = downloadurl = None
    # 字幕
    subtitle = soup.find(attrs={'kind': 'subtitles'})
    if subtitle and subtitle.has_attr('src') and str(subtitle).find("2862") == -1:
        subtitleurl = base + subtitle['src']
    # 压缩包
    download = soup.find(attrs={'title': 'Download'})
    if download and download.has_attr('href'):
        downloadurl = download['href']
    # 视频
    source = soup.find(attrs={'type': 'video/mp4'})
    if source and source.has_attr('src') and str(source).find("AskAQuestion") == -1:
        videourl = source['src']
        filename = videourl[videourl.rfind("/") + 1:videourl.rfind('?')]
        idir = todir + '/'
        filename = ititle + '.' + filename
        info.write(utf(filename) + ',' + utf(isteptitle) + ',' + utf(videourl) + ',' + utf(subtitleurl) + ',' + utf(downloadurl) + ',' + utf(iurl) + '\n')
        info.flush()
        if subtitleurl:
            q.put((subtitleurl, idir, filename.replace('mp4', 'srt')))
        if downloadurl:
            q.put((downloadurl, idir, getFilename(downloadurl)))
        q.put((videourl, idir, filename))


for i in range(5):
    t = DownloadThread()
    t.daemon = True
    t.start()
getchapter('https://teamtreehouse.com/library/' + course_name)

print '任务获取完毕'
while q.unfinished_tasks != 0 or not finish:
    time.sleep(1)
print "下载完毕"

