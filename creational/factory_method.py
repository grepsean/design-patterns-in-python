"""
Factory Method Pattern
https://ko.wikipedia.org/wiki/%ED%8C%A9%ED%86%A0%EB%A6%AC_%EB%A9%94%EC%84%9C%EB%93%9C_%ED%8C%A8%ED%84%B4

기본적으로 Abstract Factory를 오버래핑한 놈이다.
다른 점은 Abstract Factory는 각 Part를 만들어주지만, Factory Method는 객체 자체를 한방에 만들어준다.
"""


class Creator:
    def __init__(self):
        self.bike = self.make_bike()

    def make_bike(self):
        pass


class ConcreteCreatorA(Creator):
    def make_bike(self):
        return Sprinter()


class ConcreteCreatorB(Creator):
    def make_bike(self):
        return Minivelo()


class Bike:
    def __init__(self, color, size):
        self.body_color = color
        self.wheel_size = size


class Sprinter(Bike):
    def __init__(self, color, size):
        super().__init__('black', 15)


class Minivelo(Bike):
    def __init__(self, color, size):
        super().__init__('red', 12)
