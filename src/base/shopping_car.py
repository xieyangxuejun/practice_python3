#!usr/bin/python
# encoding:utf-8

"""
@author: silen
@contact: xieyangxuejun@gmail.com
@file: shopping_car.py
@time: 2018/11/23 11:53
@desc: 购物车控制台程序, 打印商品, 购买商品
@software:
@license:
"""


class ShoppingCar:
    product_list = []
    shopping_list = []
    salary = 0

    def __init__(self, product_list):
        self.salary = int(input('input your salary-->'))
        self.product_list = product_list
        self.print_product_list()

    def print_product_list(self):
        for num, p in enumerate(self.product_list):
            print("num:%d, product name:%s, price:%d" % (num, p[0], int(p[1])))

    def buy(self):
        while True:
            choice = int(input('choice product num:'))
            product = self.product_list[choice]
            if choice < len(self.product_list) and self.salary >= product[1]:
                print('-----------success---------------')
                self.shopping_list.append(product)
                self.salary -= product[1]
                print('--------------------------------last salary->%d' % self.salary)
                self.print_product_list()
            else:
                print('------------DEFAULT---------------')


if __name__ == '__main__':
    shopping_car = ShoppingCar([
        ('p1', 100),
        ('p2', 200),
        ('p3', 300),
        ('p4', 400),
        ('p5', 500),
    ])
    shopping_car.buy()
