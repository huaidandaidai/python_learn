"""
    作者：lsh
    版本：5.0
    日期：2019-01-02
    功能：
         1、把人民币换算成美元
        2、把美元换算成人民币
        3、换算过程中 不退出
        4、把程序封装进函数中
        5、使程序结构化
"""


def convert_currency(im,er):
    out = im * er
    return out


def main():
    # 汇率
    usd_vs_rmb = 6.77
    # 输入
    currency_str_value = input('请输入带有单位的货币金额:')
    # 获取货币单位
    unit = currency_str_value[-3:]

    # 判断
    if unit == 'CNY':
        exchange_rate = 1 / usd_vs_rmb
    elif unit == 'USD':
        exchange_rate = usd_vs_rmb
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        out_money = convert_currency(in_money,exchange_rate)
        print("转换后的金额：",out_money)
    else:
        print("不支持该种货币！")


if __name__ == '__main__':
    main()