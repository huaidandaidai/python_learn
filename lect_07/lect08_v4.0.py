"""
    作者：lsh
    功能：模拟掷骰子
    版本：v4.0
    日期：2019/1/16
    功能：
        v2.0：模拟掷两个骰子
        v3.0：结果可视化
        v4.0: 直方图表示
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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
    total_times = 100000


    # 记录骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)


    #  数据可视化
    plt.hist(roll_list, bins=range(2, 14),normed=1, edgecolor='black' ,linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('出现次数')
    plt.show()


if __name__ == '__main__':
    main()