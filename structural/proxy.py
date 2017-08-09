"""
Proxy pattern
https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns

Proxy는 Concrete(Real) Subject의 일부 작업을 대신해주는 패턴이다.
동일한 작업이 Proxy와 RealSubject모두 가지고 있어야하며, Subject에 의해 interface한다.

"""


class Subject:
    def action1(self):
        raise NotImplemented

    def action2(self):
        raise NotImplemented


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def action1(self):
        # ...
        self._real_subject.action1()
        # ...

    def action2(self):
        print('delegation')


class RealSubject(Subject):
    def action1(self):
        print('action1')

    def action2(self):
        print('action2')


if __name__ == '__main__':
    proxy = Proxy(RealSubject())
    proxy.action1()
    proxy.action2()
