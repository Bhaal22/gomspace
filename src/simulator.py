from src.geometry import Point
from src.robot import Robot
from src.grid import Grid, Color
from src.cardinals import WindRose

class Simulator:
    ORIGIN = Point(0, 0)
    def __init__(self):
        self.robot = Robot(Simulator.ORIGIN, WindRose.NORTH_INDEX)
        self.grid = Grid()

    
    def run(self, steps):
        for step in range(steps):
            print('Step %d' % step)
        
            original_cell = self.robot.position
            cell = self.grid.add_cell(original_cell)

            if cell.color == Color.WHITE:
                self.robot.clockwise_rotate()
            elif cell.color == Color.BLACK:
                self.robot.anti_clockwise_rotate()
        
            cell.flip()
            self.robot.move()

        print(self.grid.x_range)
        print(self.grid.y_range)

        for cell in self.grid.cells:
            print('cell: %s - color:%s' % (cell, self.grid.cells[cell].color))