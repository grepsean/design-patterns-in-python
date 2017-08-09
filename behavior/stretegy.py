"""
Strategy pattern
https://sourcemaking.com/design_patterns/strategy


OOP에서의 다형성. 기능의 선언과 구현의 기능을 분리하는 것이다.
"""


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def action(self):
        self._strategy.algorithm()


class Strategy:
    def algorithm(self):
        raise NotImplemented


class ConcreteStrategyA(Strategy):
    def algorithm(self):
        print(self.__class__.__name__)


class ConcreteStrategyB(Strategy):
    def algorithm(self):
        print(self.__class__.__name__)


if __name__ == '__main__':
    contextA = Context(ConcreteStrategyA())
    contextA.action()
    contextB = Context(ConcreteStrategyB())
    contextB.action()
