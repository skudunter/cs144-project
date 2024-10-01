import stddraw


class GUI:
    def __init__(self, size) -> None:
        self.size = size
        stddraw.setCanvasSize(800, 800)
        # Scaling the canvas to fit the grid
        stddraw.setXscale(-0.5, self.size - 0.5)
        stddraw.setYscale(-0.5, self.size - 0.5)

    def update(self, board):
        stddraw.clear()  # Clear the canvas at the beginning of every update

        for row in range(len(board)):
            for col in range(len(board[row])):
                cell = board[row][col]
                self.draw_cell(col, row, cell)

        stddraw.show()

    def draw_cell(self, x, y, cell):
        # Draw the square outline of the cell
        stddraw.square(x*80, y*80, 0.5)

        # Draw the icon/letter if the cell has an object
        if len(cell) > 0:
            icons = {'B', 'H', 'F', 'D', 'W'}
            letter = None
            for obj in cell:
                if obj.icon in icons:
                    letter = obj.icon
                    break
            if letter is None:  # Default to first object if no priority icon is found
                letter = cell[0].icon

            # Draw the letter centered in the cell
            stddraw.text(x*80, y*80, letter)
