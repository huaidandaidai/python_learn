""""
    作者：lsh
    版本：v1.0
    日期：2019-01-02
    功能：计算基础代谢率
"""


def main():
    # 性别
    gender = '男'

    # 体重（kg）
    weight = 70

    # 身高（cm）
    height = 175

    # 年龄
    age = 25

    if gender == '男':
        bmr =13.7 * weight +5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1
    if bmr !=-1:
        print("基础代谢率：", bmr)
    else:
        print("不支持该性别计算！")


if __name__ == '__main__':
    main()