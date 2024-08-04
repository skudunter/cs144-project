import stdio


class Simulation:
    def __init__(self):
        self.is_gui_mode = False
        self.size = 50
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
