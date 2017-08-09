"""
Bridge pattern
https://ko.wikipedia.org/wiki/%EB%B8%8C%EB%A6%AC%EC%A7%80_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/bridge
http://radek.io/2011/08/26/design-patterns-bridge/

abstraction과 implementation의 커플링은 없애서 서로 독립적으로 만드는 패턴이다.
런타임에 여러 implementations을 왔다갔다할때 유용하다,

"""


class Abstraction:
    def __init__(self, implementation):
        # 분리된 implementation을 관리하기 위한 참조값 저장
        self._implementation = implementation

    def operation(self):
        self._implementation.implementation()


class Implementor:
    # Abstraction과 상관없이 독립적으로 존재한다
    def implementation(self):
        raise NotImplemented


class ConcreteImplementorA(Implementor):
    def implementation(self):
        print(self.__class__.__name__)


class ConcreteImplementorB(Implementor):
    def implementation(self):
        print(self.__class__.__name__)


if __name__ == '__main__':
    concrete_implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(concrete_implementor_a)
    abstraction.operation()
