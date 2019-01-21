"""
    作者：lsh
    版本：v1.0
    日期：2019-01-02
    功能：绘制分型树
"""
import turtle


def draw_branch(branch_length):
    """
        绘制分型树
    """
    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length-10)

        # 绘制左侧树枝
        turtle.left(40)
        # 返回
        draw_branch(branch_length - 10)
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    turtle.penup()
    turtle.left(90)
    turtle.backward(200)
    turtle.pendown()
    draw_branch(80)
    turtle.exitonclick()


if __name__ == '__main__':
    main()