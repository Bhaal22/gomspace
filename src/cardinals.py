from src.geometry import Vector

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