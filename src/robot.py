from src.cardinals import WindRose

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


