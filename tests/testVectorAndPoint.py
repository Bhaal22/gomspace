import unittest
from src.main import Point, Vector


class VectorAndPointTests(unittest.TestCase):
    def test_point_and_vector_addition(self):
        p = Point(3, 5)
        v = Vector(0, 1)

        p2 = p + v
        self.assertEqual(3, p2.x)
        self.assertEqual(6, p2.y)

