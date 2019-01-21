"""
    作者：lsh
    日期：2019/01/16
    版本：v5.0
    功能：爬虫实现爬取空气质量情况
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        返回url的文本
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')

    city_aqi = get_city_aqi(city_pinyin)

    print(city_aqi)


if __name__ == '__main__':
    main()