from bee import Bee, DesertBee, HoneyBee,Wasp


class BeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'B'
        self.children = []

    def add_bee(self, bee: Bee):
        self.children.append(bee)


class DesertBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'D'

    def add_bee(self, bee: DesertBee):
        pass


class HoneyBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'H'

    def add_bee(self, bee: HoneyBee):
        pass


class WaspHive:
    def __init__(self, row: int, col: int, num_wasps: int):
        self.icon = 'W'
        self.children = []

    def add_wasp(self, wasp: Wasp):
        self.children.append(wasp)
