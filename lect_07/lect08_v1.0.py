"""
    作者：lsh
    功能：模拟掷骰子
    版本：v1.0
    日期：2019/1/14
"""
import random


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 1000000000
    # 初始化列表 [0,0,0,0,0,0]
    result_list =[0] * 6
    for i in range(total_times):
        result_list[roll_dice()-1] += 1

    # 输出
    for i, result in enumerate(result_list):
        print('点数{}的次数：{},频率：{}'.format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()