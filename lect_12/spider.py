'''
    爬虫爬取斗图吧的图片
'''
import requests
from bs4 import BeautifulSoup
from urllib import request

# 用来存储所有的页面的url
PAGE_URLS = []


def parse_page(page_url):
    # 首先先要对请求的身份进行伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                      " like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    response = requests.get(page_url, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, 'lxml')
    img_list = soup.find_all("img", attrs={"class": "img-responsive lazy img_dta"})
    for img in img_list:
        img_url = img["data-original"]
        print(img_url)
        file_name = img_url.split("/")[-1]
        full_path = os.path.join("images",file_name)
        request.urlretrieve(img_url, full_path)
        break


def main():
    # 获取所有页面的url
    for x in range(1,100):
        page_url = "http://www.doutula.com/photo/list/?page="+str(x)
        PAGE_URLS.append(page_url)

    # 获取每一页的数据
    for page_url in  PAGE_URLS:
        parse_page(page_url)


if __name__ == '__main__':
    main()