# # Напишите определение класса GroceryItem
# class GroceryItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'
#
#     def __repr__(self):
#         return f'GroceryItem({self.name}, {self.price}, {self.quantity})'
#
#
# # Ниже код для проверки методов класса GroceryItem
# banana = GroceryItem('Banana', 10, 5)
# assert banana.__str__() == """Name: Banana
# Price: 10
# Quantity: 5"""
# assert repr(banana) == 'GroceryItem(Banana, 10, 5)'
# print(banana)
# print(f"{banana!r}")
#
# dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
# assert dragon_fruit.__str__() == """Name: Dragon fruit
# Price: 5
# Quantity: 350"""
# assert repr(dragon_fruit) == 'GroceryItem(Dragon fruit, 5, 350)'
# print(dragon_fruit)
# print(f"{dragon_fruit!r}")


# Напишите определение класса Hero
class Hero:
    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        if self.__len__() == 0:
            return ''
        else:
            answer: str = ''
            for key, value in sorted(self.__dict__.items(), key=lambda para: para[0]):
                answer += f'{key}: {str(value)}\n'
            return answer.rstrip('\n')
# Ниже код для проверки методов класса Hero
hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
assert str(hero) == '''damage: 10
health: 50'''
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)

villain = Hero()
assert str(villain) == ''
assert len(villain) == 0
villain.level = 15
villain.skill = 'Боец'
villain.armor = 25
assert len(villain) == 3
assert str(villain) == '''armor: 25
level: 15
skill: Боец'''
print(villain)
