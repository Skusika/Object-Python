# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(temp):
#         temp1 = temp * 9 / 5 + 32
#         return temp1
#
#     @staticmethod
#     def fahrenheit_to_celsius(temp):
#         temp2 = (temp - 32) * 5 / 9
#         return temp2
#
#
# # Ниже код для проверки методов класса TemperatureConverter
# assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
# assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
# assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
# assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
# assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
# assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0
#
# assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
# assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
# assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
# assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
# assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
# assert TemperatureConverter.fahrenheit_to_celsius(32) == 0
# print('Good')

# class RobotVacuumCleaner:
#     name = 'Henry'
#     charge = 25
#
#     @classmethod
#     def update_charge(cls, new_value):
#         cls.charge = new_value
#
#     @staticmethod
#     def hello(name):
#         return f'Привет, {name}'
#     @property
#     def data(self):
#         return {
#             'name': self.name,
#             'charge': self.charge
#         }
#
#     @classmethod
#     def make_clean(self):
#         if self.charge < 30:
#             return 'Кожаный, заряди меня! Я слаб'
#         return 'Я вычищу твою берлогу!!!'
#
#
# # код ниже не нужно удалять, в нем находятся проверки
# print(RobotVacuumCleaner.hello('Господин'))
# RobotVacuumCleaner.update_charge(50)
#
# robot = RobotVacuumCleaner()
# print(robot.make_clean())
# print(robot.data)
#
# RobotVacuumCleaner.update_charge(False)
# print(robot.make_clean())
class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    @staticmethod
    def is_positive(number):
        if number > 0:
            return True
        else:
            return False

    @staticmethod
    def area(radius):
        s = 3.14 * radius ** 2
        return s


# код ниже не нужно удалять, в нем находятся проверки
circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 3.14
assert Circle.area(2) == 12.56