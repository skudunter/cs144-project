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
            return self.do_perception_walk()

        elif self.pollen is not None:
            return self.do_walk_to_hive()
        else:
            print("error: no condition met")
            return 0, 0

    def do_random_walk(self) -> Tuple[int, int]:
        next_trajectory = self.compass.get_next_trajectory()
        displacement = convert_radian_to_Tuple(
            next_trajectory.get_direction_in_radians())
        distance = next_trajectory.get_distance()
        new_col, new_row = int(
            displacement[0] * distance), int(displacement[1] * distance)
        return new_row + self.row, new_col + self.col

    def do_perception_walk(self) -> Tuple[int, int]:
        # walk first diagonally then horizontally or vertically to the flower
        if self.flower is None:
            print("error: flower is None")
            return 0, 0

        steps = self.compass.get_next_trajectory().get_distance()

        while steps > 0 and self.row != self.flower.row and self.col != self.flower.col:
            if self.flower.row > self.row:
                self.row += 1
            else:
                self.row -= 1

            if self.flower.col > self.col:
                self.col += 1
            else:
                self.col -= 1

            steps -= 1

        while steps > 0:
            if self.row != self.flower.row:
                if self.flower.row > self.row:
                    self.row += 1
                else:
                    self.row -= 1

            elif self.col != self.flower.col:
                if self.flower.col > self.col:
                    self.col += 1
                else:
                    self.col -= 1

            steps -= 1

        return self.row, self.col

    def do_walk_to_hive(self) -> Tuple[int, int]:
        # walk first diagonally then horizontally or vertically to the hive
        if self.home_hive is None:
            print("error: home hive is None")
            return 0, 0

        steps = self.compass.get_next_trajectory().get_distance()

        while steps > 0 and self.row != self.home_hive.row and self.col != self.home_hive.col:
            if self.home_hive.row > self.row:
                self.row += 1
            else:
                self.row -= 1

            if self.home_hive.col > self.col:
                self.col += 1
            else:
                self.col -= 1

            steps -= 1

        while steps > 0:
            if self.row != self.home_hive.row:
                if self.home_hive.row > self.row:
                    self.row += 1
                else:
                    self.row -= 1

            elif self.col != self.home_hive.col:
                if self.home_hive.col > self.col:
                    self.col += 1
                else:
                    self.col -= 1

            steps -= 1

        return self.row, self.col

    def get_distance_to_flower(self) -> float:
        return ((self.row - self.flower.row) ** 2 + (self.col - self.flower.col) ** 2) ** 0.5

    def collect_pollen(self, pollen: Pollen):
        self.pollen = pollen

    def check_if_bee_is_at_flower(self) -> bool:
        if self.flower is None:
            return False
        return self.row == self.flower.row and self.col == self.flower.col


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
