import stdio
import time


class Simulation:
    def __init__(self):
        self.is_gui_mode = False
        self.size = 50
        self.simulation_speed = 1
        self.simulation_steps = 100
        self.pollen_type = 'f'
        self.sorting_type = 'max'
        self.board = []

    def change_gui_mode(self, new_mode):
        self.is_gui_mode = new_mode

    def change_size(self, new_size):
        self.board = [[0 for i in range(new_size)] for j in range(new_size)]
        self.size = new_size

    def change_simulation_steps(self, new_simulation_steps):
        self.simulation_steps = new_simulation_steps

    def change_pollen_type(self, new_pollen_type):
        self.pollen_type = new_pollen_type

    def change_sorting_mode(self, new_sorting_mode):
        self.sorting_type = new_sorting_mode

    def get_board(self):
        return self.board

    def add_entity(self, row, col, entity):
        self.board[row][col] = entity

    def print_board(self):
        header = "    " + " ".join(f"{col:03}" for col in range(self.size))
        stdio.writeln(header)
        top_border = "   " + "+---" * self.size + "+"
        stdio.writeln(top_border)
        for row in range(self.size - 1, -1, -1):
            row_str = f"{row:03}|"
            for col in range(self.size):
                cell = self.board[row][col].icon if self.board[row][col] != 0 else 0
                if cell == 0:
                    cell = " "
                row_str += f" {cell} |"
            stdio.writeln(row_str)
            stdio.writeln(top_border)

    def is_valid_position(self, row, col):
        return self.board[row][col] == 0

    def update(self):
        for i in range(self.simulation_steps):
            time.sleep(self.simulation_speed)
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] != 0:
                        tile_entity = self.board[row][col]
                        # TODO make not so hacky
                        try:
                            for child in tile_entity.children:
                                new_row, new_col = child.get_next_move()
                                if self.is_valid_position(new_row, new_col):
                                    self.board[row][col] = 0
                                    self.board[new_row][new_col] = child
                        except:
                            pass
