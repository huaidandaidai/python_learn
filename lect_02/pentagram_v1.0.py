"""
    作者：lsh
    版本：1.0
    日期：2019-01-02
    功能：五角星绘制
"""
import turtle


def main():
    """
        主函数
    """
    count = 1
    while count <=5:
        turtle.forward(50)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()

