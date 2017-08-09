"""
Facade pattern
https://ko.wikipedia.org/wiki/%ED%8D%BC%EC%82%AC%EB%93%9C_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/facade

Facade는 여러 클래스들의 기능을 조합해서, 목적을 위해 간단히 사용할 수 있는 인터페이스를 제공한다.
"""


class LightButton1:
    def push(self):
        print('1층에 불켜짐')


class LightButton2:
    def push(self):
        print('2층에 불켜짐')


class LightButton3:
    def push(self):
        print('3층에 불켜짐')


class LightButtonPusher:
    def __init__(self):
        self.button1 = LightButton1()
        self.button2 = LightButton2()
        self.button3 = LightButton3()

    def push_all(self):
        self.button1.push()
        self.button2.push()
        self.button3.push()
