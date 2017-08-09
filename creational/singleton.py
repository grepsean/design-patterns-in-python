"""
Singleton
https://ko.wikipedia.org/wiki/%EC%8B%B1%EA%B8%80%ED%84%B4_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/singleton

생성자가 여러번 호출되더라도 오직 하나의 인스턴스만을 리턴해준다. 없으면 새로 만들어서 리턴해줌.
"""


class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        return cls._instance
