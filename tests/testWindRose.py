import unittest
from src.main import WindRose


class WindRoseTests(unittest.TestCase):
    def test_turn_clockwise_from_north(self):
        v, i = WindRose.clockwise_rotate(0)
        self.assertEqual(v, WindRose.EAST)

    def test_turn_clockwise_from_west(self):
        v, i = WindRose.clockwise_rotate(3)
        self.assertEqual(v, WindRose.NORTH)

    def test_turn_anti_clockwise_from_north(self):
        v, i = WindRose.anti_clockwise_rotate(0)
        self.assertEqual(v, WindRose.WEST)
