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

    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)