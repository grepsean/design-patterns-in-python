"""
Decorator pattern
https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/decorator

동적으로 책임을 추가하는 패턴 (파이썬의 decorator를 상상해도 된다)
주어진 상황 및 용도에 따라 어떤 객체에 책임을 덧붙이는 패턴으로, 기능 확장이 필요할 때 서브클래싱 대신 쓸 수 있는 유연한 대안이 될 수 있다.

"""


class AbstractBike:
    """
    동적으로 책임을 추가할 클래스에 인터페이스를 정의한다.
    """

    def pedaling(self):
        raise NotImplemented


class BikeDecorator(AbstractBike):
    def __init__(self, bike):
        self._bike = bike

    def pedaling(self):
        raise NotImplemented


class ConcreteBikeDecoratorChargeBattery(BikeDecorator):
    def pedaling(self):
        self.start_charge_battery()
        self._bike.pedaling()  # origin method 위 혹은 아래에 책임을 넣을 수 있다
        self.end_charge_battery()

    def start_charge_battery(self):
        print('충전 시작')

    def end_charge_battery(self):
        print('충전 중지')


class ConcreteBikeDecoratorLight(BikeDecorator):
    def pedaling(self):
        self.light_on()
        self._bike.pedaling()
        self.light_off()

    def light_on(self):
        print('Light On')

    def light_off(self):
        print('Light Off')


class ConcreteBike(AbstractBike):
    def pedaling(self):
        print('따르릉')


if __name__ == '__main__':
    bike = ConcreteBike()
    bike_decorator_a = ConcreteBikeDecoratorChargeBattery(bike)
    bike_decorator_b = ConcreteBikeDecoratorLight(bike_decorator_a)
    bike_decorator_b.pedaling()
