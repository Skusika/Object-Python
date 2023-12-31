from collections import defaultdict
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return (f'Пользователь {self.login}, баланс - {self.balance}')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, number):
        self.__balance += number

    def payment(self, digit):
        if self.__balance < digit:
            print(f'Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= digit
            return True


class Cart:
    def __init__(self, user):
        self.__total = 0
        self.goods = defaultdict()
        if isinstance(user, User):
            self.user = user

    def add(self, product, count=1):
        if isinstance(product, Product):
            self.goods[product] = self.goods.get(product, 0) + count
            self.__total += (count * product.price)

    def remove(self, product, count=1):
        if isinstance(product, Product):
            if count > self.goods[product]:
                count = self.goods[product]
                self.goods[product] = self.goods.get(product, 0) - count
                self.__total -= count * product.price

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        sorted_lst = sorted(self.goods, key=lambda x: x.name)
        print("---Your check---")
        for elem in sorted_lst:
            if self.goods[elem] > 0:
                print(f'{elem.name} {elem.price} {self.goods[elem]} {self.goods[elem] * elem.price}')
        print(f"---Total: {self.__total}---")

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)
cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20






billy = User('billy@rambler.ru')
print(billy) # Пользователь billy@rambler.ru, баланс - 0
billy.deposit(100)
billy.deposit(300)
print(billy) # Пользователь billy@rambler.ru, баланс - 400
billy.payment(500) # Не хватает средств на балансе. Пополните счет
billy.payment(150)
print(billy) # Пользователь billy@rambler.ru, баланс - 250

