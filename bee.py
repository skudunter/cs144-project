from compass import Compass
import math


class Bee:
    def __init__(self, row: int, col: int, speed: int, perception: int,home_hive = None):
        self.icon = 'b'
        self.row = row
        self.col = col
        self.compass = Compass(row, col, speed)
        self.flower = None
        self.perception = perception
        self.home_hive = home_hive

    def get_next_move(self):
        if self.flower is None:
            return self.do_random_walk()
        else:
            return self.do_perception_walk()

    def do_random_walk(self):
        next_trajectory = self.compass.get_next_trajectory()
        displacement = convert_radian_to_tuple(
            next_trajectory.get_direction_in_radians())
        distance = next_trajectory.get_distance()
        new_col, new_row = int(
            displacement[0] * distance), int(displacement[1] * distance)
        return new_row + self.row, new_col + self.col

    def do_perception_walk(self):
        # TODO implement this
        flower_row, flower_col = self.flower.get_position()
        row, col = self.compass.get_position()
        if abs(flower_row - row) <= self.perception and abs(flower_col - col) <= self.perception:
            return self.do_random_walk()
        else:
            return self.do_perception_walk()


class Wasp(Bee):
    def __init__(self, row: int, col: int, speed: int):
        super().__init__(row, col, speed, perception=0,home_hive=None)
        self.icon = 'w'


class HoneyBee(Bee):
    def __init__(self, row: int, col: int, speed: int, perception: int,home_hive=None):
        super().__init__(row, col, speed, perception,home_hive=None)
        self.icon = 'h'


class DesertBee(Bee):
    def __init__(self, row: int, col: int, speed: int, perception: int,home_hive=None):
        super().__init__(row, col, speed, perception,home_hive=None)
        self.icon = 'd'


def convert_radian_to_tuple(radians):
    return (round(math.cos(radians)), round(math.sin(radians)))
