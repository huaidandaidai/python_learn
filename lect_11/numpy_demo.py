"""
    作者:lsh
    版本：v1.0
    日期：2019-01-25
    功能：numpy练习-数组创建
"""
import numpy as np


def main():
    """
        主函数
    """
    # 创建一维数组
    arr1 = np.array([1, 2, 3])
    print(arr1)

    # 创建二维数组
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr2)

    # 使用arange函数创建包含0到9 十个数字的以为数组
    arr_1 = np.arange(10)
    arr_1[3:5] = 10
    print('haha', arr_1)
    arr_2 = np.arange(1, 10, 2)
    print(arr_1)
    print(arr_2)

    # 全0 全1数组
    # 创建一个长度为10 的全0 一维数组
    z1 = np.zeros(10)
    print(z1)
    # 创建一个3行4列的二维全0 数组
    z2 = np.zeros((3, 4))
    print(z2)

    # 创建一个长度为5的全0 一维数组
    o1 = np.ones(5)
    print(o1)
    # 创建3行4列全1二位数组
    o2 = np.ones((3, 4))
    print(o2)
    print(np.arange(99, 0, -2))


if __name__ == '__main__':
    main()


