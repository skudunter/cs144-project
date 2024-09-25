import stdio
import time
from bee import Bee


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
        self.board = [[[] for _ in range(new_size)] for _ in range(new_size)]
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
        self.board[row][col].append(entity)

    def print_board(self):
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

    def get_cell_display(self, cell):
        # make sure that hives and flowers get priority
        if len(cell) == 0:
            return " "
        icons = {'B', 'H', 'F', 'D', 'W'}
        for obj in cell:
            if obj.icon in icons:
                return obj.icon
        return cell[0].icon

    def is_valid_position(self, row, col):
        return len(self.board[row][col]) == 0

    def update(self):
        for i in range(self.simulation_steps):
            self.print_board()
            time.sleep(self.simulation_speed)
            placeholder_board = [
                [[] for _ in range(self.size)] for _ in range(self.size)]
            for row in range(self.size):
                for col in range(self.size):
                    for object in self.board[row][col]:
                        if isinstance(object, Bee):
                            self.move_bee(object, placeholder_board)
                        else:
                            placeholder_board[row][col].append(object)    
            self.board = placeholder_board


    def move_bee(self, object: Bee, placeholder_board):
        new_row, new_col = object.get_next_move()
        new_row = max(0, min(new_row, self.size - 1))
        new_col = max(0, min(new_col, self.size - 1))
        object.row = new_row
        object.col = new_col
        placeholder_board[new_row][new_col].append(object)
