from compass import Compass
from beehive import BeeHive
from flower import Pollen, Flower
from typing import Tuple
import math


class Bee:
    def __init__(self, row: int, col: int, speed: int, perception: int, home_hive: BeeHive):
        self.icon = 'b'
        self.row = row
        self.col = col
        self.compass = Compass(row, col, speed)
        self.flower: Flower = None
        self.perception = perception
        self.home_hive = home_hive
        self.pollen: Pollen = None

    def get_next_move(self) -> Tuple[int, int]:
        # returns a tuple(int, int) of the next move according to the bee's state
        if (self.flower is None) and (self.pollen is None):
            return self.do_random_walk()

        elif (self.flower is not None) and (self.pollen is None):
            return self.do_walk_to_target(self.flower)

        elif self.pollen is not None:
            return self.do_walk_to_target(self.home_hive)
        else:
            print("error: no condition met")
            return 0, 0

    def do_random_walk(self) -> Tuple[int, int]:
        next_trajectory = self.compass.get_next_trajectory()
        displacement = convert_radian_to_Tuple(
            next_trajectory.get_direction_in_radians())
        distance = next_trajectory.get_distance()
        d_col, d_row = int(
            displacement[0] * distance), int(displacement[1] * distance)
        return d_row, d_col

    def do_walk_to_target(self, target: Flower) -> Tuple[int, int]:
        # walk first diagonally then horizontally or vertically to the target
        d_row, d_col = 0, 0
        if target is None:
            print("error: target is None")
            return d_row, d_col

        distance = self.compass.get_next_trajectory().get_distance()

        if distance > 0 and self.row != target.row and self.col != target.col:
            if target.row > self.row:
                d_row = distance
            else:
                d_row = -distance

            if target.col > self.col:
                d_col = distance
            else:
                d_col = -distance
        elif distance > 0:
            if self.row != target.row:
                if target.row > self.row:
                    d_row = distance
                else:
                    d_row = -distance

            elif self.col != target.col:
                if target.col > self.col:
                    d_col = distance
                else:
                    d_col = -distance

        return d_row, d_col

    def get_distance_to_flower(self) -> float:
        return math.floor(((self.row - self.flower.row) ** 2 + (self.col - self.flower.col) ** 2) ** 0.5)

    def collect_pollen(self, pollen: Pollen):
        self.pollen = pollen

    def check_if_bee_is_at_flower(self) -> bool:
        if self.flower is None:
            return False
        return self.row == self.flower.row and self.col == self.flower.col

    def check_if_bee_is_at_hive(self) -> bool:
        if self.home_hive is None:
            return False
        return self.row == self.home_hive.row and self.col == self.home_hive.col


class Wasp(Bee):
    def __init__(self, row: int, col: int, speed: int):
        super().__init__(row, col, speed, perception=0, home_hive=None)
        self.icon = 'w'


class HoneyBee(Bee):
    def __init__(self, row: int, col: int, speed: int, perception: int, home_hive):
        super().__init__(row, col, speed, perception, home_hive)
        self.icon = 'h'


class DesertBee(Bee):
    def __init__(self, row: int, col: int, speed: int, perception: int, home_hive):
        super().__init__(row, col, speed, perception, home_hive)
        self.icon = 'd'


def convert_radian_to_Tuple(radians):
    return (round(math.cos(radians)), round(math.sin(radians)))
