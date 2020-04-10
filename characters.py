# The super() function lets us call a bit of code from the parent class
# inside our own class. This is really helpful when you need to override a method
# from the superclass, defining your own version, but keep the effects of the parent class's version of the code.

import random


class Character:
    def __int__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10
