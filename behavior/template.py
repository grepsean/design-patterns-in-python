"""
Template Method Pattern
https://sourcemaking.com/design_patterns/template_method

상위 클래스에서 처리의 흐름을 제어하며, 하위클래스에서 처리의 내용을 구체화한다.
즉, 상위 클래스에서 아직 구현되지 않은 동작을 비어있는 template method로 만들어놓고,
하위 클래스에서 해당 template method를 구현하는 것이다.
코드의 중복을 줄이고, Refactoring에 유리한 패턴으로 상속을 통한 확장 개발 방법으로써 전략 패턴(Strategy Pattern)과 함께 가장 많이 사용되는 패턴중에 하나이다.
"""


class AbstractClass:
    def template_method(self):
        self._operation1()
        self._operation_2()

    def _operation1(self):
        raise NotImplemented

    def _operation_2(self):
        raise NotImplemented


class ConcreteClass(AbstractClass):
    def _operation1(self):
        print('Operation1')

    def _operation_2(self):
        print('Operation2')


def main():
    concrete_class = ConcreteClass()
    concrete_class.template_method()
