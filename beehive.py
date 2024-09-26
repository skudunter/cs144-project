class BeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'B'
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col


class DesertBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'D'


class HoneyBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'H'


class WaspHive:
    def __init__(self, row: int, col: int, num_wasps: int):
        self.icon = 'W'
