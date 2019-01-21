"""
    作者：lsh
    版本：v1.0
    日期：2019-01-21
    功能：小象全球购
"""

# 全局变量：商品列表
goods_dict = {"001": {"name": "爱马仕腰带", "price": 1999},
              "002": {"name": "劳力士男表", "price": 19999},
              "003": {"name": "巴宝莉眼镜", "price": 4999},
              "004": {"name": "路虎发现四", "price": 99999},
              "005": {"name": "圣罗兰", "price": 256},
              "006": {"name": "神仙水", "price": 784}
              }


shopping_car_list = []


def print_goods_dict():
    """
        打印商品列表
    """
    print("--------------------商品列表--------------------")
    print("商品编号", " " * 10, "商品名称", " " * 10, "商品价格")
    for key, value in goods_dict.items():
        print(key, " " * 10, value["name"], " " * 10, value["price"])


def add_to_shopping_car():
    """
        将商品添加到购物车
    """
    print_goods_dict()
    goods_serial_number = input("请根据商品列表信息输入商品编号，退出购物请输入Q：")
    while goods_serial_number != "Q":
        if goods_serial_number in goods_dict.keys():
            buy_number = input("请输入您要购买的数量：")
            if buy_number.isnumeric() and eval(buy_number) > 0:
                shopping_car_list.append((goods_serial_number, buy_number))
                goods_serial_number = ''
                continue
            elif buy_number.isnumeric() and eval(buy_number) == 0:
                goods_serial_number = ''
                continue
            else:
                continue

        if goods_serial_number != '':
            print("商品编号不存在，请重新输入！")
        print_goods_dict()
        goods_serial_number = input("请根据商品列表信息输入商品编号，退出购物请输入Q：")


def pay():
    """
        支付购物车内的商品
    """
    print("-----------欢迎您来到订单结算页面--------------")
    print("您当前的购物车商品信息为：")
    pay_amount = 0
    for buy_goods in shopping_car_list:
        goods_serial_number = buy_goods[0]
        buy_number = buy_goods[1]
        goods = goods_dict[goods_serial_number]
        pay_amount += float(goods["price"]) * float(buy_number)
        print("商品名称：{}，商品单价：{}，数量：{}，商品总价：{}".format(goods["name"], goods["price"], buy_number, float(goods["price"]) * float(buy_number)))
    print("订单金额：{}".format(pay_amount))
    pay_str = input("请您付款：")
    pay_result = False
    while pay_result is False:
        if pay_str.isnumeric() and 0 < eval(pay_str) < pay_amount:
            print("付款失败，输入金额小于订单总额！")
            pay_str = input("请您付款：")
        elif pay_str.isnumeric() and eval(pay_str) >= pay_amount:
            pay_result = True
            print("付款成功，找您{}元！".format(eval(pay_str) - pay_amount))
        else:
            print("付款失败，请输入合法金额！")
            pay_str = input("请您付款：")


def main():
    """
        主程序
    """
    add_to_shopping_car()
    if len(shopping_car_list) > 0:
        pay()
    else:
        print("-----------本次购物结束，期待您的下次光临--------------")


if __name__ == '__main__':
    main()