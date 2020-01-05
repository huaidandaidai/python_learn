# coding:utf-8
import lxml.html
import random
import time
import requests


class CsdnSpider():
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
    ]
    url_list = [
        "https://blog.csdn.net/huaidandaidai1/article/details/103747236",
        "https://blog.csdn.net/huaidandaidai1/article/details/103651774",
        "https://blog.csdn.net/huaidandaidai1/article/details/103542407",
        "https://blog.csdn.net/huaidandaidai1/article/details/98214155",
        "https://blog.csdn.net/huaidandaidai1/article/details/103150237",
        "https://blog.csdn.net/huaidandaidai1/article/details/103150237",
        "https://blog.csdn.net/huaidandaidai1/article/details/102999954",
        "https://blog.csdn.net/huaidandaidai1/article/details/102652341",
        "https://blog.csdn.net/huaidandaidai1/article/details/99125338",
        "https://blog.csdn.net/huaidandaidai1/article/details/99083272",
        "https://blog.csdn.net/huaidandaidai1/article/details/82146896",
        "https://blog.csdn.net/huaidandaidai1/article/details/100049761",
        "https://blog.csdn.net/huaidandaidai1/article/details/100057856",
        "https://blog.csdn.net/huaidandaidai1/article/details/100049779",
        "https://blog.csdn.net/huaidandaidai1/article/details/99576175",
        "https://blog.csdn.net/huaidandaidai1/article/details/96623159",
        "https://blog.csdn.net/huaidandaidai1/article/details/95030507",
        "https://blog.csdn.net/huaidandaidai1/article/details/93329687"
    ]

    def __init__(self):
        self.page = 0
        self.proxy = []

    def get_proxy(self):
        self.page += 1
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        request = requests.get("https://www.kuaidaili.com/free/inha/" + str(self.page), headers=headers)
        html = request.content
        etree = lxml.html.etree
        content = etree.HTML(html)
        # print html
        ip = content.xpath('//td[@data-title="IP"]/text()')
        port = content.xpath('//td[@data-title="PORT"]/text()')
        # 将对应的ip和port进行拼接
        for i in range(len(ip)):
            for p in range(len(port)):
                if i == p:
                    if ip[i] + ':' + port[p] not in self.proxy:
                        self.proxy.append(ip[i] + ':' + port[p])
        # print self.proxy
        if self.proxy:
            print("this use" + str(self.page) + "page IP")
            self.spider()

    def spider(self):
        num = 0  # 用于访问计数
        err_num = 0  # 用于异常错误计数
        while True:
            # 从列表中随机选择UA和代理
            user_agent = random.choice(self.USER_AGENTS)
            proxy = random.choice(self.proxy)

            referer = random.choice(self.url_list)  # 随机选择访问url地址
            headers = {
                "Host": "blog.csdn.net",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Referer": "https://blog.csdn.net/huaidandaidai1",
                "User-Agent": user_agent,
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=40BB_WJznlUTst_x5zXyO8qyfEHBfz5XeH1mvTvy_BCwJUZAJ40h6g3WRKOucWGpYIVTQzsV-vh9TB05MDcUaxCX4kKqjMmSxAfMDJ5oIqi&wd=&eqid=e6951e1e00019ed1000000025e114eb8; uuid_tt_dd=10_19289143580-1572748911127-243932; dc_session_id=10_1572748911127.737122; UN=huaidandaidai1; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19289143580-1572748911127-243932!5744*1*huaidandaidai1; Hm_lvt_546e1cab6a063d7a69c8c546554525c7=1572788214; Hm_ct_546e1cab6a063d7a69c8c546554525c7=5744*1*huaidandaidai1!6525*1*10_19289143580-1572748911127-243932; __gads=Test; Hm_lvt_146e5663e755281a5bbe1f3f1c477685=1573907632; Hm_ct_146e5663e755281a5bbe1f3f1c477685=5744*1*huaidandaidai1!6525*1*10_19289143580-1572748911127-243932; UM_distinctid=16e77b3046f4e6-048092c94c0fb5-e343166-144000-16e77b30470480; Hm_lvt_875750bb60be42b670a3dcbe49cac301=1574859009; Hm_ct_875750bb60be42b670a3dcbe49cac301=5744*1*huaidandaidai1!6525*1*10_19289143580-1572748911127-243932; __yadk_uid=HVstCyCdAcp4eOrMUdnZ8Ev8C4bLzORb; UserName=huaidandaidai1; UserInfo=cb4e2a80e1ff46fa91e7ad73dff6af82; UserToken=cb4e2a80e1ff46fa91e7ad73dff6af82; UserNick=%E5%9D%8F%E8%9B%8B%E5%91%86%E5%91%86; AU=5A6; BT=1578056904294; p_uid=U000000; firstDie=1; acw_tc=2760820115781446055096526eba7ef05cfb33505bbd475dd45423f27907f9; TY_SESSION_ID=a3283e7e-8122-48bd-8c63-d6f9a308759b; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1578191150,1578191174,1578192572,1578192643; acw_sc__v2=5e1154b43850038d4ad1671d9f4f5abed885e660; acw_sc__v3=5e1154b4396ab42a3a29bbfe5a80ffcc45e210a3; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F103603408%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; dc_tos=q3m7ci; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1578195379"
            }
            try:
                # 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
                request = requests.get(referer, headers=headers, proxies={"http": proxy})
                html = request.content
                etree = lxml.html.etree
                content = etree.HTML(html)
                # 使用xpath匹配阅读量
                read_num = content.xpath('//span[@class="read-count"]/text()')
                # 将列表转为字符串
                new_read_num = ''.join(read_num)
                # 通过xpath匹配的页面为blog.csdn.net/qq_41782425/article/details/84934224所以匹配其他页面返回的为空
                if len(new_read_num) != 0:
                    print(new_read_num)

                num += 1
                print('The' + str(num) + 'few visits')
                print(request.url + "proxy ip: " + str(proxy))
                # print request.headers
                time.sleep(6)
                # 当访问数量达到100时，退出循环，并调用get_proxy方法获取第二页的代理
                if num > 100:
                    break
            except Exception as result:
                err_num += 1
                print("error message(%d):%s" % (err_num, result))
                # 当错误信息大于等于30时，初始化代理页面page，重新从第一页开始获取代理ip，并退出循环
                if err_num >= 30:
                    self.__init__()
                    break
        # 当退出循环时，看就会执行get_proxy获取代理的方法
        print("Re acquiring agent proxy IP")
        self.get_proxy()


if __name__ == "__main__":
    CsdnSpider().get_proxy()
