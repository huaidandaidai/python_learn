"""
    作者:lsh
    版本：v1.0
    日期：2019-01-22
    功能：爬取双色球
"""
import requests
from bs4 import BeautifulSoup


def get_batch_number():
    """
        获取期数
    """
    url = "http://kaijiang.500.com/shtml/ssq/19009.shtml"
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    number_div = soup.find_all('div',{'class': 'iSelectList'})[0]
    number_links = number_div.find_all("a")
    batch_number_list = []
    for link in number_links:
        batch_number = link.text
        batch_number_link = link['href']
        batch_number_list.append((batch_number, batch_number_link))
    return batch_number_list


def get_double_chromosphere(batch_number_list):

    for batch_number in batch_number_list:
        r = requests.get(batch_number[1], timeout=30)
        soup = BeautifulSoup(r.text, 'lxml')
        number_div = soup.find_all('div', {'class': 'ball_box01'})[0]
        red_ball_li = number_div.find_all('li', {'class': 'ball_red'})
        blue_ball = number_div.find_all('li', {'class': 'ball_blue'})[0].text
        red_ball_list = []
        for red_ball in red_ball_li:
            red_ball_list.append(red_ball.text)

        print("期数：",batch_number[0],"红球：",red_ball_list, "蓝球：", blue_ball)


def main():
    """
        主函数
    """
    batch_number_list = get_batch_number()
    get_double_chromosphere(batch_number_list)


if __name__ == '__main__':
    main()