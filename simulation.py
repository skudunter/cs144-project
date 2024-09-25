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
        # TODO implement multiple things on one cell business
        if len(cell) == 0:
            return " "
        return cell[0].icon

    def is_valid_position(self, row, col):
        return len(self.board[row][col]) == 0

    def update(self):
        for i in range(self.simulation_steps):
            self.print_board()
            time.sleep(self.simulation_speed)
            for row in range(self.size):
                for col in range(self.size):
                    for object in self.board[row][col]:
                        print(type(object).__name__)
                        if (type(object).__name__ == "Bee"):
                            self.move_bee(object)

    def move_bee(self,object):
        new_row, new_col = object.get_next_move()
        if (new_row < 0):
            new_row = 0
        if (new_col < 0):
            new_col = 0
        if (new_row >= self.size):
            new_row = self.size - 1
        if (new_col >= self.size):
            new_col = self.size - 1
        self.board[object.row][object.col].remove(object)
        object.row = new_row
        object.col = new_col
        self.board[new_row][new_col].append(object)
