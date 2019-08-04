"""
    作者:lsh
    版本：v1.0
    日期：2019-07-20
    功能：刷新csdn博客访问量
"""

import re
import time
import random
import requests
import urllib.request
from bs4 import BeautifulSoup

firefoxHead = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
IPRegular = r"(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])"
host = "https://blog.csdn.net"
url = "https://blog.csdn.net/huaidandaidai1/article/details/{}"
codes = ["96604426", "94360543", "95030507", "81298925", "93329687",
         "93228862", "93329720", "92794759", "86543776", "81222547",
         "81670382", "81698425", "82191395", "81979704", "81432127",
         "81257161", "81408925", "81387025", "81257112", "81180663",
         "81160111", "81056651", "81004338", "80960573", "80875088",
         "80820208", "80789492", "98458213", "96623159", "96604426"]


def parseIPList(url="http://www.xicidaili.com/"):
    IPs = []
    request = urllib.request.Request(url, headers=firefoxHead)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, "lxml")
    tds = soup.find_all("td")
    for td in tds:
        string = str(td.string)
        if re.search(IPRegular, string):
            IPs.append(string)
    return IPs


def PV():
    s = requests.Session()
    s.headers = firefoxHead
    count = 0
    while True:
        count += 1
        print("正在进行第{}次访问\t".format(count), end="\t")
        IPs = parseIPList()
        s.proxies = {"http": "{}:8080".format(IPs[random.randint(0, 40)])}
        s.get(host)
        r = s.get(url.format(codes[random.randint(0, 27)]))
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        spans = soup.find_all("span")
        print(spans[2].string)
        time.sleep(random.randint(60, 120))


def main():
    PV()

    
if __name__ == '__main__':
    main()