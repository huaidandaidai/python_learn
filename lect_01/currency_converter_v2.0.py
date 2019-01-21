"""
    作者：lsh
    版本：2.0
    日期：2018-12-29“
    功能：
        1、把人民币换算成美元
        2、把美元换算成人民币
"""
# 汇率
usd_vs_rmb = 6.77
# 输入
currency_str_value = input('请输入带有单位的货币金额:')
# 获取货币单位
unit = currency_str_value[-3:]

# 判断
if unit == 'CNY':
    rmb_str_value = currency_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / usd_vs_rmb
    print("美元(USD)金额是： ", usd_value)
elif unit == 'USD':
    usd_str_value = currency_str_value[:-3]
    usd_value = eval(usd_str_value)
    rmb_value = usd_value * usd_vs_rmb
    print("人民币(CNY)金额是： ", rmb_value)
else:
    print("当前版本暂不支持当前货币的转换！")