from typing import Any

# TODO think of polymorphism

class Pollen:
    def __init__(self, information: Any):
        pass

class Flower:
    def __init__(self, row: int, col: int, pollen_type: str):
        self.icon = 'F'

    def add_pollen(self, pollen: Pollen):
        pass


class Bee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        self.icon = 'b'
       


class BeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'B'

    def add_bee(self, bee: Bee):
        pass


class DesertBee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        self.icon = 'd'


class DesertBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'D'

    def add_bee(self, bee: DesertBee):
        pass


class HoneyBee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        self.icon = 'h'


class HoneyBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'H'

    def add_bee(self, bee: HoneyBee):
        pass


class Wasp:
    def __init__(self, row: int, col: int, speed: int):
        self.icon = 'w'


class WaspHive:
    def __init__(self, row: int, col: int, num_wasps: int):
        self.icon = 'W'

    def add_wasp(self, wasp: Wasp):
        pass


class Map:
    def __init__(self, size: int):
        pass

    def add_beehive(self, beehive: BeeHive):
        pass

    def add_desert_beehive(self, beehive: DesertBeeHive):
        pass

    def add_honey_beehive(self, beehive: HoneyBeeHive):
        pass

    def add_wasphive(self, wasphive: WaspHive):
        pass

    def add_flower(self, flower: Flower):
        pass
