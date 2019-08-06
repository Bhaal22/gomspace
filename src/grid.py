from enum import Enum
import math

class Color(Enum):
    BLACK = 0
    WHITE = 1


class Cell:
    def __init__(self):
        self.color = Color.WHITE

    def flip(self):
        if self.color == Color.WHITE:
            self.color = Color.BLACK
            return
        elif self.color == Color.BLACK:
            self.color = Color.WHITE
            return

        raise Exception("Unsupported Cell::color %s" % self.color)

class Grid:
    def __init__(self):
        self.x_range = (math.inf, -math.inf)
        self.y_range = (math.inf, -math.inf)
        self.cells = {}

    def add_cell(self, position):
        cell = self.cells.get(position)

        if cell is None:
            cell = Cell()
            self.cells[position] = cell
        
        self.x_range = (min(self.x_range[0], position.x), max(self.x_range[1], position.x))
        self.y_range = (min(self.y_range[0], position.y), max(self.y_range[1], position.y))

        return cell