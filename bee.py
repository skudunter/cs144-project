from compass import Compass
class Bee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        self.icon = 'b'
        self.compass = Compass(row, col, speed)

    def move(self):
        next_trajectory = self.compass.get_next_trajectory()
        print(next_trajectory)


class Wasp:
    def __init__(self, row: int, col: int, speed: int):
        self.icon = 'w'


class HoneyBee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        self.icon = 'h'


class DesertBee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        self.icon = 'd'
