""""
    作者：lsh
    版本：v3.0
    日期：2019-01-03
    功能：计算基础代谢率
        增加 一行输入全部信息
        增加 带单位输出
"""


def main():
    print('请输入一下信息，用空格分割')
    input_str = input('性别 体重(kg) 身高(cm) 年龄：')
    str_list = input_str.split(' ')
    gender = str_list[0]
    weight = float(str_list[1])
    height = float(str_list[2])
    age = int(str_list[3])

    if gender == '男':
        bmr =13.7 * weight +5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1
    if bmr != -1:
        print("您的性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}".format(gender,weight,height,age))
        print("基础代谢率：{}大卡".format(bmr))
    else:
        print("不支持该性别计算！")


if __name__ == '__main__':
    main()