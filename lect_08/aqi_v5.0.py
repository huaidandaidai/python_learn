"""
    作者：lsh
    日期：2019/01/16
    版本：v5.0
    功能：爬虫实现爬取空气质量情况
"""
import requests


def get_html_test(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_test(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index:end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()