"""
    作者:lsh
    版本：v1.0
    日期：2019-01-22
    功能：爬取双色球
"""
import requests
from bs4 import BeautifulSoup


def get_batch_number():
    url = "http://kaijiang.500.com/shtml/ssq/"
    batch_number = []
    for i in range(3001, 19009):
        if len(str(i)) == 4:
            batch_number.append("0" + str(i))
        else:
            batch_number.append(str(i))
    return batch_number


def get_double_chromosphere(batch_number):

    for num in batch_number:
        r = requests.get('http://kaijiang.500.com/shtml/ssq/'+num+'.shtml', timeout=30)
        soup = BeautifulSoup(r.text, 'lxml')
        number_div = soup.find_all('div', {'class': 'ball_box01'})[0]
        red_ball_li = number_div.find_all('li', {'class': 'ball_red'})
        blue_ball = number_div.find_all('li', {'class': 'ball_blue'})[0].text
        red_ball_list = []
        for red_ball in red_ball_li:
            red_ball_list.append(red_ball.text)

        print("期数：",num,"红球：",red_ball_list, "蓝球：", blue_ball)


def main():
    """
        主函数
    """
    url = "http://kaijiang.500.com/shtml/ssq/"
    batch_number = get_batch_number()
    get_double_chromosphere(batch_number)


if __name__ == '__main__':
    main()