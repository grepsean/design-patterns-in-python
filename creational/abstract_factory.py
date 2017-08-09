"""
https://ko.wikipedia.org/wiki/%EC%B6%94%EC%83%81_%ED%8C%A9%ED%86%A0%EB%A6%AC_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/abstract_factory

Abstract Factory의 목적은 concrete class를 정의하지 않고 관련된 객체들를 생성하는 인터페이스를 제공하는 것이다
concrete class에는 객체를 구성할 각 파트들에 대한 알고리즘을 구현한다.
"""


class AbstractBikeFactory:
    def make_body(self):
        raise NotImplemented

    def make_wheel(self):
        raise NotImplemented

    def make(self):
        bike = Bike()
        bike.body_color = self.make_body()
        bike.wheel_size = self.make_wheel()
        return bike


class ConcreteBikeFactoryA(AbstractBikeFactory):
    def make_body(self):
        return 'red'

    def make_wheel(self):
        return 12


class ConcreteBikeFactoryB(AbstractBikeFactory):
    def make_body(self):
        return 'black'

    def make_wheel(self):
        return 15


class Bike:
    def __init__(self, color, size):
        self.body_color = color
        self.wheel_size = size
