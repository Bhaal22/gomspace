from src.geometry import Point
from src.robot import Robot
from src.grid import Grid, Color
from src.cardinals import WindRose
from src.geometry import Point

class Simulator:
    ORIGIN = Point(0, 0)
    def __init__(self):
        self.robot = Robot(Simulator.ORIGIN, WindRose.NORTH_INDEX)
        self.grid = Grid()

    
    def run(self, steps):
        step = 0
        if steps < 0:
            raise Exception('number of steps must be positive(%d)' % steps)

        while step < steps:
            print('Step %d' % step)
        
            original_cell = self.robot.position
            cell = self.grid.add_cell(original_cell)

            if cell.color == Color.WHITE:
                self.robot.clockwise_rotate()
            elif cell.color == Color.BLACK:
                self.robot.anti_clockwise_rotate()
        
            cell.flip()
            self.robot.move()
            step = step + 1

    def export_grid(self, filename):
        print('export_grid')

        print(self.grid.x_range)
        print(self.grid.y_range)

        for cell in self.grid.cells:
            print('cell: %s - color:%s' % (cell, self.grid.cells[cell].color))
        
        x_min = self.grid.x_range[0] - 2
        x_max = self.grid.x_range[1] + 2
        y_min = self.grid.y_range[0] - 2
        y_max = self.grid.y_range[1] + 2

        with open(filename, "w") as simulation_file:
            simulation_file.write('x range: [%d,%d]\n' % (x_min, x_max))
            simulation_file.write('y range: [%d,%d]\n' % (y_min, y_max))
            simulation_file.write('\n')

            y = y_max
            while y >= y_min:
                simulation_file.write('|')
                x = x_min
                while x <= x_max:
                    cell = self.grid.cells.get(Point(x, y))
                    if cell is None or cell.color == Color.WHITE:
                        simulation_file.write('W|')
                    elif cell.color == Color.BLACK:
                        simulation_file.write('B|')
                    x = x + 1
                y = y - 1
                simulation_file.write('\n')