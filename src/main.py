class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Point(self.x + vector.x, self.y + vector.y)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    