"""
Visitor pattern

각 Visotor가 여러 Visitable에 visit하는 패턴으로, Visotor의 알고리즘을 객체 구조(Visitable)와 분리시키는 방법이다.
Visitable의 수정 없이도, Visitor를 변경하거나 다른 Visitor를 구현해서 accept시켜주면 된다.
"""


class Visitable:
    def accept(self, visitor):
        visitor.visit(self)


class Visitor:
    def visit(self, visitable):
        raise NotImplemented


class Cart(Visitable):
    def __init__(self):
        self.items = [
            ItemA(), ItemB()
        ]

    def accept(self, visitor):
        print('Cart accepted')
        visitor.visit(self)
        for item in self.items:
            item.accept(visitor)


class ItemA(Visitable):
    def accept(self, visitor):
        print('ItemA accepted')
        visitor.visit(self)


class ItemB(Visitable):
    def accept(self, visitor):
        print('ItemB accepted')
        visitor.visit(self)


class Shopper(Visitor):
    def visit(self, visitable):
        if visitable.__class__ == Cart:
            print('Cart visited')
        elif visitable.__class__ == ItemA:
            print('ItemA visited')
        elif visitable.__class__ == ItemB:
            print('ItemB visited')


if __name__ == '__main__':
    cart = Cart()
    cart.accept(Shopper())
