class Robot:

    def set_name(self, name):
        self.name = name
    def say_hello(self):
        if hasattr(self, 'name') == True:
            print(f"Hello, human! My name is {name}")
        else:
            print(f'У робота нет имени')

    def say_bye(self):
        print("See u later alligator")


c3po = Robot()
r2d2 = Robot()
c3po.say_hello()
c3po.say_bye()
r2d2.say_hello()
r2d2.say_bye()
