"""
https://ko.wikipedia.org/wiki/%EB%B9%8C%EB%8D%94_%ED%8C%A8%ED%84%B4

복잡한 단계가 필요한 객체의 생성과정을 Builder로 추상화하고, Director가 이 Builder를 통해 간단하게 make할 수 있게 해준다.

Director에게 Builder(주문서)의 내용을 채워주면, Director.make()를 통해서 Builder의 내용(주문서)으로 build해서 객체를 생성해준다.
주문서(AbstractBuilder)에는 각 part를 만드는 방법(color, size)이 빈칸(Abstract)으로 되어있다.
이 주문서를 채워서(구현해서) Director에게 주면 되는 것이다.
"""


class Director:
    def __init__(self, builder=None):
        self.builder = builder

    def set_builder(self, builder):
        self.builder = builder

    def make(self):
        self.builder.build()


class AbstractBuilder:
    def __init__(self):
        self.bike = Bike()

    def set_body_color(self):
        pass

    def set_wheel_size(self):
        pass

    def build(self):
        self.set_body_color()
        self.set_wheel_size()
        return self.bike


class ConcreteBuilderA(AbstractBuilder):
    def set_body_color(self):
        self.bike.body_color = 'black'

    def set_wheel_size(self):
        self.bike.wheel_size = 22


class ConcreteBuilderB(AbstractBuilder):
    def set_body_color(self):
        self.bike.body_color = 'red'

    def set_wheel_size(self):
        self.bike.wheel_size = 18


class Bike:
    def __init__(self, color, size):
        self.body_color = color
        self.wheel_size = size
