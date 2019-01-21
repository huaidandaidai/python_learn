"""
    作者：lsh
    版本：v1.0
    日期：2019-01-04
    功能：52周存钱挑战
"""

def main():
    """
        主函数
    """
    money_per_week = 10         # 每周的存入的金额
    i = 1                        # 记录周数
    increase_money = 10         # 递增的金额
    total_week = 52             # 总共的周数
    saving = 0                  # 账户累计

    while i <= total_week:
        saving += money_per_week
        print('第{}周，存入{}元，账户累计{}元'.format(i,money_per_week,saving))
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()