from enum import Enum
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        if isinstance(vector, Vector):
            return Point(self.x + vector.x, self.y + vector.y)
        
        raise TypeError("Point Addition supported only with Vector (%s)" % type(vector))

    def __eq__(self, obj):
        return isinstance(obj, Point) and obj.x == self.x and obj.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, obj):
        return isinstance(obj, Vector) and obj.x == self.x and obj.y == self.y


class WindRose:
    NORTH = Vector(0, 1)
    NORTH_INDEX = 0

    EAST = Vector(1, 0)
    EAST_INDEX = 1

    SOUTH = Vector(0, -1)
    SOUTH_INDEX = 2

    WEST = Vector(-1, 0)
    WEST_INDEX = 3

    ORIENTATIONS = [ NORTH, EAST, SOUTH, WEST ]

    @staticmethod
    def clockwise_rotate(index):
        next = (index + 1) % 4
        return WindRose.ORIENTATIONS[next], next

    @staticmethod
    def anti_clockwise_rotate(index):
        next = (index - 1) % 4
        return WindRose.ORIENTATIONS[next], next


class Robot:
    def __init__(self, position, move_orientation_index):
        self.position = position
        self.move_orientation_index = move_orientation_index
        self.move_orientation = WindRose.ORIENTATIONS[move_orientation_index]

    def clockwise_rotate(self):
        print('clockwise from %s' % self.position)
        self.move_orientation, self.move_orientation_index = WindRose.clockwise_rotate(self.move_orientation_index)

    def anti_clockwise_rotate(self):
        print('anti_clockwise from %s' % self.position)
        self.move_orientation, self.move_orientation_index = WindRose.anti_clockwise_rotate(self.move_orientation_index)

    def move(self):
        self.position = self.position + self.move_orientation

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
        
        cell.flip()
        self.x_range = (min(self.x_range[0], position.x), max(self.x_range[1], position.x))
        self.y_range = (min(self.y_range[0], position.y), max(self.y_range[1], position.y))

        return cell


def game():
    origin = Point(0, 0)
    robot = Robot(origin, WindRose.NORTH_INDEX)
    grid = Grid()

    for step in range(10):
        print('Step %d' % step)
        print('Robot position %s' % robot.position)
        grid.add_cell(robot.position)
        robot.move()
        print('Robot position %s' % robot.position)

        cell = grid.cells.get(robot.position)
        if cell.color == Color.WHITE:
            robot.clockwise_rotate()
        elif cell.color == Color.BLACK:
            robot.anti_clockwise_rotate()

    print(grid.x_range)
    print(grid.y_range)

    for cell in grid.cells:
        print('cell: %s - color:%s' % (cell, grid.cells[cell].color))

