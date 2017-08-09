"""
Adapter pattern
https://ko.wikipedia.org/wiki/%EC%96%B4%EB%8C%91%ED%84%B0_%ED%8C%A8%ED%84%B4
https://sourcemaking.com/design_patterns/adapter

220V -> 어댑터를 통해서 -> 110V로 변경하는 거다.
기존 클래스를 건드리지 않고, 동일한 기능이지만, (강화된) 기능을 추가하거나 변경하는 것이다.

"""


class BikeGear:
    def __init__(self):
        self.max_gear = 21
        self.current_gear = 1

    def shift_up(self):
        self.current_gear += 1


class BikeGearSafer:
    def __init__(self, bike_gear):
        self.bike_gear = bike_gear

    def safe_shift_up(self):
        raise NotImplemented


class Adapter(BikeGearSafer):
    def __init__(self, bike_gear):
        super().__init__(bike_gear)
        if not self.bike_gear:
            self.bike_gear = BikeGear()

    def safe_shift_up(self):
        if self.bike_gear.max_gear == self.bike_gear.current_gear:
            raise Exception('can\' shift up')
        else:
            self.bike_gear.shift_up()
