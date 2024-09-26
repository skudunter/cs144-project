from typing import Any, List


class Pollen:
    def __init__(self, information: Any):
        self.information = information


class Flower:
    def __init__(self, row: int, col: int, pollen_type: str):
        self.icon = 'F'
        self.pollen_type = pollen_type
        self.pollens: List[Pollen] = []
        self.row = row
        self.col = col

    def add_pollen(self, pollen: Pollen):
        self.pollens.append(pollen)

    def get_pollen_length(self):
        return len(self.pollens)

    def get_pollen(self):
        return self.pollens.pop()

    def get_position(self):
        return self.row, self.col
