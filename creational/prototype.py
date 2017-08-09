"""
Prototype pattern
https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%ED%86%A0%ED%83%80%EC%9E%85_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/prototype

새로 생성할 객체를 프로토타입 객체로 결정하게 하는 것이다. 즉, 새로운 객체를 만들때 자기 자신을 복사해서 만든다.
상황에 따라 deepcopy가 필요할 수 있다.
"""

import copy


class Bike:
    def __init__(self, color, size):
        self.body_color = color
        self.wheel_size = size


class PrototypeBike(Bike):
    def __str__(self):
        return 'color: {}, wheel: {}'.format(self.body_color, self.wheel_size)

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    prototype = PrototypeBike(color='black', size=15)
    print(prototype)
    my_bike = prototype.clone()
    my_bike.body_color = 'red'
    print(my_bike)
