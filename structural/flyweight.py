"""
Flyweight pattern
https://ko.wikipedia.org/wiki/%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%9B%A8%EC%9D%B4%ED%8A%B8_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/flyweight

Flyweight는 동일한 것을 공유해서 객체 생성을 줄여 가볍게 만드는 것입니다.
내용이 동일한 객체를 FlyweightFactory에 {key: 객체} 형태로 저장해두고, key로 가져오는 전략이다.
이때 key는 객체를 구분할 수 있는 유일한 구분자여야한다. (dict를 사용)
"""
from collections import defaultdict


class CoffeeShop:  # FlyweightFactory
    def __init__(self):
        self._menu = defaultdict(lambda: None)
        self.orders = []

    def get_coffee(self, menu):
        if not self._menu[menu]:
            self._menu[menu] = CoffeeMenu(menu)
        return self._menu[menu]

    def take_order(self, menu, table_no):
        self.orders.append([self.get_coffee(menu), table_no])


class BaseCoffeeMenu:  # Flyweight
    def __init__(self, name):
        self.name = name

    def serve_coffee(self, table_no):
        raise NotImplemented


class CoffeeMenu(BaseCoffeeMenu):  # Concrete Flyweight
    def serve_coffee(self, table_no):
        print('{}번 고객님! 주문하신 {}({}) 나왔습니다.'.format(table_no, self.name, self.__hash__()))


if __name__ == '__main__':
    coffee_shop = CoffeeShop()
    coffee_shop.take_order('아메리카노', 5)
    coffee_shop.take_order('카페라떼', 5)
    coffee_shop.take_order('카페모카', 1)
    coffee_shop.take_order('아메리카노', 1)
    coffee_shop.take_order('아메리카노', 3)
    coffee_shop.take_order('카페라떼', 3)
    coffee_shop.take_order('카페모카', 3)

    for coffee_order in coffee_shop.orders:
        coffee, table_no = coffee_order
        coffee.serve_coffee(table_no)
