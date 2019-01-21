"""
    作者：lsh
    版本：3.0
    日期：2019-01-02
    功能：
        1、五角星绘制
        2、绘制多个五角星
        3、递归用法
"""
import turtle


def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    if size <= 200:
        size += 20
        draw_pentagram(size)


def main():
    """
        主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    draw_pentagram(50)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
