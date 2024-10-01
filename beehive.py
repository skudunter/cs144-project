from flower import Pollen
from typing import List


class BeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'B'
        self.row = row
        self.col = col
        self.pollens: List[Pollen] = []

    def get_position(self):
        return self.row, self.col

    def collect_pollen(self, pollen: Pollen):
        if pollen is None:
            return
        self.pollens.append(pollen)

    def get_pollen_list(self) -> List[Pollen]:
        return self.pollens


class DesertBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'D'


class HoneyBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        self.icon = 'H'


class WaspHive:
    def __init__(self, row: int, col: int, num_wasps: int):
        self.icon = 'W'
