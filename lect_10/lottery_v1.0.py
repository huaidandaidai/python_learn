"""
    作者:lsh
    版本：v1.0
    日期：2019-01-22
    功能：爬取双色球
"""
import requests
from bs4 import BeautifulSoup
import csv


def get_batch_number():
    """
        获取期数
    """
    url = "http://kaijiang.500.com/shtml/ssq/19009.shtml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                      " like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    r = requests.get(url, timeout=30, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    number_div = soup.find_all('div',{'class': 'iSelectList'})[0]
    number_links = number_div.find_all("a")
    batch_number_list = []
    for link in number_links:
        batch_number = link.text
        batch_number_link = link['href']
        batch_number_list.append((batch_number, batch_number_link))
    return batch_number_list


def get_lottery(batch_number):
    r = requests.get(batch_number[1], timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    number_div = soup.find_all('div', {'class': 'ball_box01'})[0]
    red_ball_li = number_div.find_all('li', {'class': 'ball_red'})
    blue_ball = number_div.find_all('li', {'class': 'ball_blue'})[0].text
    red_ball_list = []
    for red_ball in red_ball_li:
        red_ball_list.append(red_ball.text)
    row = [batch_number[0]] + red_ball_list + [blue_ball]
    return row


def get_double_chromosphere(batch_number_list):
    header = ['期数', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '蓝球']
    with open('lottery.csv', 'w', encoding='utf-8', newline='') as f:
        print("-----------打开文件---------------")
        writer = csv.writer(f)
        writer.writerow(header)
        print("-----------写入头---------------")
        for i, batch_number in enumerate(batch_number_list):
            if (i + 1) % 10 == 0:
                print('已处理{}记录。(共{}条记录)'.format(i + 1, len(batch_number_list)))
            row = get_lottery(batch_number)
            writer.writerow(row)


def main():
    """
        主函数
    """
    batch_number_list = get_batch_number()
    get_double_chromosphere(batch_number_list)


if __name__ == '__main__':
    main()