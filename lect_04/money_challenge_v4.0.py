"""
    作者：lsh
    版本：v4.0
    日期：2019-01-08
    功能：52周存钱挑战
        2.0新增功能：记录每周的存款数
        3.0新增功能：使用循环直接计数
        4.0新增功能：灵活设置灭纣的存款次数，增加的存款次数以及存款周数
"""
import math


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    money_list = []  # 记录每周存款数的列表

    for i in range(total_week):
        # 存钱操作
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))

        # 更新下一周的存钱金额
        money_per_week += increase_money


def main():
    """
        主函数
    """
    money_per_week = eval(input('请输入初始周存入的金额：'))         # 每周的存入的金额
    increase_money = eval(input('请输入每周递增存入的金额：'))         # 递增的金额
    total_week = eval(input('请输入总共存入的周数：'))             # 总共的周数
    save_money_in_n_weeks(money_per_week, increase_money, total_week)


if __name__ == '__main__':
    main()