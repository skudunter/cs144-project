import stdio
import time
from bee import Bee, Wasp
from beehive import WaspHive, BeeHive
from flower import Flower
import math
from typing import List, Tuple


class Simulation:
    def __init__(self):
        self.is_gui_mode = False
        self.size = 50
        self.simulation_speed = 0
        self.simulation_steps = 100
        self.pollen_type = 'f'
        self.sorting_type = 'max'
        self.board = []

    def change_gui_mode(self, new_mode: bool):
        self.is_gui_mode = new_mode

    def change_size(self, new_size: int):
        self.board = [[[] for _ in range(new_size)] for _ in range(new_size)]
        self.size = new_size

    def change_simulation_steps(self, new_simulation_steps: int):
        self.simulation_steps = new_simulation_steps

    def change_pollen_type(self, new_pollen_type: str):
        self.pollen_type = new_pollen_type

    def change_sorting_mode(self, new_sorting_mode: str):
        self.sorting_type = new_sorting_mode

    def get_board(self) -> List[List[List]]:
        return self.board

    def add_entity(self, row: int, col: int, entity):
        self.board[row][col].append(entity)

    def print_board(self):
        # print the board to console
        header = "    " + " ".join(f"{col:03}" for col in range(self.size))
        stdio.writeln(header)
        top_border = "   " + "+---" * self.size + "+"
        stdio.writeln(top_border)
        for row in range(self.size - 1, -1, -1):
            row_str = f"{row:03}|"
            for col in range(self.size):
                cell = self.get_cell_display(self.board[row][col])
                row_str += f" {cell} |"
            stdio.writeln(row_str)
            stdio.writeln(top_border)

    def get_cell_display(self, cell: List[Bee]) -> str:
        # make sure that hives and flowers get priority
        if len(cell) == 0:
            return " "
        icons = {'B', 'H', 'F', 'D', 'W'}
        for obj in cell:
            if obj.icon in icons:
                return obj.icon
        return cell[0].icon

    def is_valid_position(self, row, col) -> bool:
        return len(self.board[row][col]) == 0

    def update(self):
        # update the simulation for the number of steps
        self.print_board()
        for _ in range(self.simulation_steps):
            # remove this for final submission
            # time.sleep(self.simulation_speed)

            placeholder_board = [
                [[] for _ in range(self.size)] for _ in range(self.size)]

            for row in range(self.size):
                for col in range(self.size):
                    for obj in self.board[row][col]:
                        if isinstance(obj, Bee) and not isinstance(obj, Wasp):
                            # Assign flowers before any movement
                            self.asign_flower_to_bee(obj)

            # First pass: Move bees and copy other objects
            for row in range(self.size):
                for col in range(self.size):
                    for obj in self.board[row][col]:
                        if isinstance(obj, Bee):
                            self.move_bee(obj, placeholder_board)
                        else:
                            placeholder_board[row][col].append(obj)

            # Second pass: Handle interactions (wasps, flowers, hives)
            for row in range(self.size):
                for col in range(self.size):
                    cell_objects = placeholder_board[row][col]
                    contains_wasp = any(isinstance(obj, Wasp)
                                        for obj in cell_objects)
                    contains_wasp_hive = any(isinstance(
                        obj, WaspHive) for obj in cell_objects)

                    if contains_wasp or contains_wasp_hive:
                        placeholder_board[row][col] = [
                            obj for obj in cell_objects
                            if isinstance(obj, Wasp) or (not isinstance(obj, Bee) or (isinstance(obj, Bee) and obj.check_if_bee_is_at_hive()))
                        ]

                    for obj in cell_objects:
                        if isinstance(obj, Bee) and not isinstance(obj, Wasp):
                            self.de_asign_flower_to_bee(obj)
                            self.asign_flower_to_bee(obj)

                            # Flower pollen collection logic
                            if obj.flower and obj.check_if_bee_is_at_flower():
                                num_bees_at_flower = sum(isinstance(o, Bee) and not isinstance(
                                    o, Wasp) and o.flower == obj.flower for o in cell_objects)
                                available_pollen = obj.flower.get_pollen_length()

                                if num_bees_at_flower <= available_pollen:
                                    pollen = obj.flower.get_pollen()
                                    if pollen:
                                        obj.collect_pollen(pollen)
                                else:
                                    obj.flower = None

                            # Hive pollen collection logic
                            if obj.check_if_bee_is_at_hive():
                                obj.home_hive.collect_pollen(obj.pollen)
                                obj.pollen = None

            self.board = placeholder_board
            self.print_board()

    def move_bee(self, bee: Bee, placeholder_board: List[List[List]]):
        # get the next move and update the bee's position
        d_row, d_col = bee.get_next_move()
        # new_row, new_col = self.constrain_bee_position(bee, d_row, d_col)
        new_row, new_col = bee.row + d_row, bee.col + d_col
        bee.row = max(0, min(new_row, self.size - 1))
        bee.col = max(0, min(new_col, self.size - 1))
        placeholder_board[bee.row][bee.col].append(bee)

    # def constrain_bee_position(self, bee: Bee, d_row: int, d_col: int) -> Tuple[int, int]:
    #     # constrain the bee's position to the board boundaries
    #     new_row = bee.row + d_row
    #     new_col = bee.col + d_col

    #     if d_row != 0 and d_col == 0:
    #         if new_row < 0:
    #             new_row = 0
    #         elif new_row >= self.size:
    #             new_row = self.size - 1

    #     elif d_col != 0 and d_row == 0:
    #         if new_col < 0:
    #             new_col = 0
    #         elif new_col >= self.size:
    #             new_col = self.size - 1

    #     elif d_row != 0 and d_col != 0:
    #         if new_row < 0:
    #             ratio = bee.row / abs(d_row) if d_row != 0 else float('inf')
    #             new_row = 0
    #             new_col = int(bee.col + d_col * ratio)
    #         elif new_row >= self.size:
    #             ratio = (self.size - 1 - bee.row) / \
    #                 abs(d_row) if d_row != 0 else float('inf')
    #             new_row = self.size - 1
    #             new_col = int(bee.col + d_col * ratio)

    #         if new_col < 0:
    #             ratio = bee.col / abs(d_col) if d_col != 0 else float('inf')
    #             new_col = 0
    #             new_row = int(bee.row + d_row * ratio)
    #         elif new_col >= self.size:
    #             ratio = (self.size - 1 - bee.col) / \
    #                 abs(d_col) if d_col != 0 else float('inf')
    #             new_col = self.size - 1
    #             new_row = int(bee.row + d_row * ratio)

    #     return new_row, new_col

    def asign_flower_to_bee(self, bee: Bee):
        # if the bee is close enough to a flower, asign the flower to the bee
        for row in range(self.size):
            for col in range(self.size):
                for obj in self.board[row][col]:
                    if isinstance(obj, Flower):
                        distance = math.floor(((bee.row - row) ** 2 +
                                               (bee.col - col) ** 2) ** 0.5)
                        if distance <= bee.perception and obj.get_pollen_length() > 0:
                            if bee.flower is not None:
                                if distance < bee.get_distance_to_flower():
                                    bee.flower = obj
                                    return
                            else:
                                bee.flower = obj
                                return

    def de_asign_flower_to_bee(self, bee: Bee):
        # if the bee is too far from the flower or the flower has no pollen, de-asign the flower
        if bee.flower and (bee.get_distance_to_flower() > bee.perception or bee.flower.get_pollen_length() == 0):
            bee.flower = None

    def make_summary(self):
        # get the pollen information based on the sorting type and make a summary
        pollens = [pollen for row in self.board for col in row
                   for obj in col if isinstance(obj, BeeHive)
                   for pollen in obj.get_pollen_list() if pollen is not None]

        stdio.writeln("Answer:")
        if not pollens:
            stdio.writeln("No pollen collected")
            return

        if self.sorting_type == 'max':
            max_pollen = max(pollens, key=lambda x: x.information).information
            stdio.writeln(max_pollen)
        elif self.sorting_type == 'min':
            min_pollen = min(pollens, key=lambda x: x.information).information
            stdio.writeln(min_pollen)
        elif self.sorting_type == 'sum':
            total_information = sum(pollen.information for pollen in pollens)
            stdio.writeln(total_information)
        elif self.sorting_type == 'sort':
            pollens.sort(key=lambda x: x.information)
            for pollen in pollens:
                stdio.writeln(pollen.information)
