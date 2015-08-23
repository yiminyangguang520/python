__author__ = 'Wong Tzuchiang'
import requests
import re
import threading
import os

http_agent = 'http://user:password@hk2.nhpass.com:110'
proxies = {'http': http_agent, 'https': http_agent, }
proxies = None
http_agent_backup = 'http://user:password@hk1.nhpass.com:110'
proxies_backup = {'http': http_agent, 'https': http_agent, }


class DownloadThread(threading.Thread):
    def __init__(self, canshu_url, canshu_flodoer, canshu_name, canshu_proxy):
        threading.Thread.__init__(self)
        self.url = canshu_url
        self.flodoer = canshu_flodoer
        self.name = canshu_name
        self.proxy = canshu_proxy

    def run(self):
        print("start downloading " + self.name)

        r = requests.get(self.url, proxies=self.proxy)
        with open(self.flodoer + "\\" + self.name, "wb") as code:
            code.write(r.content)
            print("downloading " + self.name + " successfully")


s = requests.session()
s.headers["Cookie"] = "_treehouse_session=b1Z6QmEyeHVaSjBZYy92aWtlWExYMDZJOE9rQktKTjEwa2dhT0hsMENncU4rRHJjc0sra0ZidnhSU1RHNkdYQnhONWxXcGhRTG9aR0ZBbFhuRERrbkFjbHN5QjVJNmIwTkZhaUZwdmVTL1JZMnBkZ3NhV3E1Y29PNkUzQVdXZTRVa1VDOXc1bDV3WGV0NU4xQS9WVEpRRlFOenZGV2pvTjNYOTZQRXRFNTh6TE1nelV1Y2RCUThBczdmb3hhRURuQ2Q5dlBXQVFINjUyYUl2N3hSQTdvRzJlL1Fybkg4bVl2amg4MmNCNDRpbDJjK2VOWTBwbCtsRlBiN05Rbm1Wdkxoc3IwK1ljTWE1M3FBdTYyYzlCSlEzaXJ3Zkd5UHRYMXRYYnBYMERUb3JyYXJIU1UzNGhJZGdQVFBHSGlaYXB2blFjUklxajVabWNQMG03U0ZvZkl2V3QxZ1lJNFcvd3Ntd0JKNEZGaFJuMVM1aXV2bVNDMTRIQk1kQTVDYXI1RzNOVitQT0tlTkJtUVFkazdiOUtYYWpFbVNFdnE2MUhYTVhCRjliaFd1N0FmNWZDa0ZjZUdYRkhOYXFjcDM0ZS0tZUg0MWN5aGN2YkJudUZQQkhGTDR0dz09--4158435b72e736e2ed84dee1443cb88c0859858e; path=/; HttpOnly"
html = s.get("http://teamtreehouse.com/library/objectivec-basics", proxies=proxies).text

match_index = re.compile(
    r'<li>[\s\S]{1,10}<a href="(/library/objectivec-basics.*?)">[\s\S]{1,10}<span class="icon icon-video"></span>[\s\S]*?<p>[\s\S]*?</p>[\s\S]*?<strong>([\s\S]*?)</strong>[\s\S]*?</a></li>')
match_download = re.compile(
    r'" type="video/webm" /><source src="(https://videos.teamtreehouse.com/videos/([\s\S]*?)\?token=[\s\S]*?)" type="video/mp4" /><track kind="subtitles" src="([\s\S]*?)" srclang="en" /></video>')
match_subtitle = re.compile(r'attachment; filename="([\s\S]*?)"')
match_appendix = re.compile(r'<a class="button-reveal" href="([\s\S]*)" title="Download">')

Result_index = match_index.findall(html)
# print(Result_index)
for i in range(len(Result_index)):
    url_index = "http://teamtreehouse.com" + Result_index[i][0]
    html = s.get(url_index, proxies=proxies).text
    Result_download = match_download.findall(html)
    Result_appendix = match_appendix.findall(html)
    # print(html)
    # print(Result_download)
    # print(Result_appendix)
    url_download_mp4 = Result_download[0][0]
    url_download_subtitle = "http://teamtreehouse.com" + Result_download[0][2]
    # print (html)

    if Result_appendix:
        url_download_appendix = Result_appendix[0]

    r = s.get(url_download_subtitle, proxies=proxies, stream=True)
    Result_subtitle = match_subtitle.findall(r.headers["content-disposition"])

    saving_name_floder = Result_index[i][1]
    saving_name_floder = saving_name_floder.strip()
    saving_name_mp4 = Result_download[0][1]
    saving_name_subtitle = Result_subtitle[0]
    if Result_appendix:
        saving_name_appendix = url_download_appendix[url_download_appendix.rfind('/') + 1:]
    strinfo = re.compile(r':')
    saving_name_floder = strinfo.sub('', saving_name_floder)

    path = "d:\\pachong\\" + str(i) + "." + saving_name_floder

    strinfo = re.compile(r'\?')

    path = strinfo.sub('', path)
    saving_name_subtitle = strinfo.sub('', saving_name_subtitle)
    a = 1
    # print( path)
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isfile(path + "\\" + saving_name_mp4):
        if a == 1:
            thread = DownloadThread(url_download_mp4, path, saving_name_mp4, proxies)
            thread.start()
            a = 0
        elif a == 0:
            thread = DownloadThread(url_download_mp4, path, saving_name_mp4, proxies_backup)
            thread.start()
            a = 1

    if not os.path.isfile(path + "\\" + saving_name_subtitle):
        thread = DownloadThread(url_download_subtitle, path, saving_name_subtitle, proxies)
        thread.start()

    if Result_appendix:
        if not os.path.isfile(path + "\\" + saving_name_appendix):
            # print(saving_name_appendix)
            thread = DownloadThread(url_download_appendix, path, saving_name_appendix, proxies)
            thread.start()
