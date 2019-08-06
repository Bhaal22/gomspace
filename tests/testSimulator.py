import unittest
from src.grid import Color
from src.cardinals import WindRose
from src.simulator import Simulator

class SimulatorTests(unittest.TestCase):
    def test_simultor_1_step(self):
        simulator = Simulator()

        simulator.run(1)

        self.assertEqual(len(simulator.grid.cells), 1)

        element = list(simulator.grid.cells.keys())[0]
        
        self.assertEqual(element, Simulator.ORIGIN)
        self.assertEqual(simulator.grid.cells[element].color, Color.BLACK)

        self.assertEqual(simulator.robot.move_orientation, WindRose.EAST)

    def test_simultor_2_steps(self):
        simulator = Simulator()

        simulator.run(2)

        self.assertEqual(len(simulator.grid.cells), 2)

        for cell in simulator.grid.cells:
            self.assertEqual(simulator.grid.cells[cell].color, Color.BLACK)