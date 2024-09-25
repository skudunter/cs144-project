from typing import Any
class Pollen:
    def __init__(self, information: Any):
        self.information = information


class Flower:
    def __init__(self, row: int, col: int, pollen_type: str):
        self.icon = 'F'
        self.pollen_type = pollen_type
        self.children = []
        self.row = row
        self.col = col

    def add_pollen(self, pollen: Pollen):
        self.children.append(pollen)
    
    def get_position(self):
        return self.row, self.col


