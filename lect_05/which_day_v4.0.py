"""
    作者：lsh
    版本：4.0
    日期：2019-01-08
    功能：输入某年某月某日，判断这一天是这一年的第几天？
        2.0增加功能：用list替换元组tuple
        3.0增加功能：使用set替换list
        4.0增加功能：使用dict替换set
"""
from datetime import datetime


def is_leap_year(year):
    """
        判断year是否为闰年
        是,返回true
        否，返回false
    """
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return  is_leap


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    # # 包含30天 月份集合
    # _30_days_month_set = {4, 6, 9, 11}
    # _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 30,
                      9: 31,
                      10: 30,
                      11: 31,
                      12: 30}

    # 初始化值
    days = day
    for i in range(1, month):
        if i in month_day_dict:
            days += month_day_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1
    print('这是{}年的第{}天！'.format(year, days))


if __name__ == '__main__':
    main()