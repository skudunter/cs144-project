import stddraw


class GUI:
    def __init__(self):
        stddraw.setCanvasSize(700, 700)
        stddraw.setXscale(0, 700)
        stddraw.setYscale(0, 700)

    def draw(self, x, y):
        stddraw.point(x, y)

    def show(self):
        stddraw.show()

test = GUI()
test.draw(350, 350)
test.show()