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

firefoxHead = {"Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cookie": "l=AurqcPuigwQdnQv7WvAfCoR1OlrRQW7h; isg=BHp6mNB79CHqYXpVEiRteXyyyKNcg8YEwjgLqoRvCI3ddxqxbLtOFUBGwwOrZ3ad; thw=cn; cna=VsJQERAypn0CATrXFEIahcz8; t=0eed37629fe7ef5ec0b8ecb6cd3a3577; tracknick=tb830309_22; _cc_=UtASsssmfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=981798063989731689; hng=CN%7Czh-CN%7CCNY%7C156; um=0712F33290AB8A6D01951C8161A2DF2CDC7C5278664EE3E02F8F6195B27229B88A7470FD7B89F7FACD43AD3E795C914CC2A8BEB1FA88729A3A74257D8EE4FBBC; enc=1UeyOeN0l7Fkx0yPu7l6BuiPkT%2BdSxE0EqUM26jcSMdi1LtYaZbjQCMj5dKU3P0qfGwJn8QqYXc6oJugH%2FhFRA%3D%3D; ali_ab=58.215.20.66.1516409089271.6; mt=ci%3D-1_1; cookie2=104f8fc9c13eb24c296768a50cabdd6e; _tb_token_=ee7e1e1e7dbe7; v=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;` rv:47.0) Gecko/20100101 Firefox/47.0"
}
firefoxHead2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
IPRegular = r"(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])"
host = "https://blog.csdn.net"
url = "https://blog.csdn.net/huaidandaidai1/article/details/{}"
# codes = ["96604426",    "93329687",
#          "93228862", "93329720", "86543776", "81222547",
#          "81979704",
#          "81257161", "81408925", "81387025", "81180663",
#          "81160111",  "80875088",
#           "80789492",  "96623159", "99576175"]

codes = ["96604426", "100049779", "94360543", "95030507", "81298925", "93329687",
         "93228862", "93329720", "92794759", "86543776", "81222547", "99125338",
         "81670382", "81698425", "82191395", "81979704", "81432127", "82146896",
         "81257161", "81408925", "81387025", "81257112", "81180663", "100049761",
         "81160111", "81056651", "81004338", "80960573", "80875088", "100057856",
         "80820208", "80789492", "98458213", "96623159", "99576175", "99083272"]


def parseIPList(url="http://www.xicidaili.com/"):
    IPs = []
    request = urllib.request.Request(url, headers=firefoxHead2)
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
        for code in codes:
            r = s.get(url.format(code))
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            spans = soup.find_all("span")
            print(spans)
            # print(spans[2].string, end="\t")
            # time.sleep(random.randint(4, 10))
        print()
        time.sleep(random.randint(60, 120))


def main():
    PV()

    
if __name__ == '__main__':
    main()