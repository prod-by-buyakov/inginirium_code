import math


class Car:
    def sound(self):
        print("beep")

    def long_sound(self):
        print("bep-beep")


class Button:
    _click = 0

    def click(self):
        self._click += 1

    def click_count(self):
        return self._click

    def reset(self):
        self._click -= self._click


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def per(self) -> int:
        return  self.a+self.c+self.b


    def square(self):
        p = self.per() / 2
        s = math.sqrt(p*(p-self.a)*(p - self.b)*(p- self.c))
        return s
    def is_prym(self):
        if self.c ** 2 + self.b**2:
            return  True
        elif self.c** 2 + self.a ** 2 == self.b ** 2:
            return True
        elif self.a ** 2 == self.c ** 2 + self.b ** 2:
            return  True
        return False
t = Triangle(3,4,5)
print(t.is_prym())


