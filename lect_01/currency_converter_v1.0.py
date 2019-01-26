"""
    作者：lsh
    版本：1.0
    日期：2018-01-02
    功能：将人民币换算成美元
"""
rmb_str_value = input('请输入人民币(CNY)金额:')
usd_vs_rmb = 6.77
usd_value = eval(rmb_str_value) / usd_vs_rmb
values = 40-3**2+11//3**2*8
# 输出
print('美元(USD)金额是： ', values)