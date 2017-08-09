"""
Observer pattern
https://ko.wikipedia.org/wiki/%EC%98%B5%EC%84%9C%EB%B2%84_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/observer

안드로이드에서 이벤트(버튼 등) 처리하는 방식.
Observer를 등록해두고, 등록받은 쪽에서 이벤트가 발생하면, 등록되어 있는 observer들에게 모두 notify해주는 디자인 패턴이다.
"""


class Subject:
    def __init__(self):
        self._obervers = []

    def attach(self, observer):
        self._obervers.append(observer)

    def detach(self, observer):
        self._obervers.remove(observer)

    def notify(self):
        for observer in self._obervers:
            if hasattr(observer, 'update'):
                observer.update(self)


class Observer:
    def update(self, subject):
        raise NotImplemented


class BikeMarket(Subject):
    def tell_me_price(self):
        self.notify()


class BikeManagerA(Observer):
    def update(self, subject):
        print('Price is Good enough')


class BikeManagerB(Observer):
    def update(self, subject):
        print('Price is High then before')


if __name__ == '__main__':
    market = BikeMarket()
    market.attach(BikeManagerA())
    market.attach(BikeManagerB())
    market.tell_me_price()
