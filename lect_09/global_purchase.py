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
    goods_num = input("请根据商品列表信息输入商品编号，退出购物请输入Q：")
    while goods_num != "Q":
        if goods_num in goods_dict.keys():
            buy_num = input("请输入您要购买的数量：")
            if eval(buy_num) > 0:
                shopping_car_list.append((goods_num, buy_num))
                goods_num = ''
                continue
            elif eval(buy_num) == 0:
                print("商品编号不存在，请重新输入！")
                print_goods_dict()
                goods_num = input("请根据商品列表信息输入商品编号，退出购物请输入Q：")

        print("商品编号不存在，请重新输入！")
        print_goods_dict()
        goods_num = input("请根据商品列表信息输入商品编号，退出购物请输入Q：")


def pay():
    """
        支付购物车内的商品
    """
    print("-----------欢迎您来到订单结算页面--------------")
    print("您当前的购物车商品信息为：")
    for i in shopping_car_list:
        goods_buy = shopping_car_list[i]
        goods_num = goods_buy[0]
        print("商品名称：{}，商品单价：{}，数量：{}，商品总价：{}".format(goods_dict[goods_num]["name"], goods_dict[goods_num]["price"], goods_buy[1],goods_dict[goods_num]["price"] * goods_buy[1]))
    print("订单金额：".format(10000))
    pay_str = input("请您付款：")



def main():
    """
        主程序
    """
    add_to_shopping_car()
    # if len(shopping_car_list) > 0:
    #     pay()
    # else:
    #     print("-----------本次购物结束，期待您的下次光临--------------")


if __name__ == '__main__':
    main()