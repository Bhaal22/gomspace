import unittest
from src.main import Point, Vector


class VectorAndPointTests(unittest.TestCase):
    def test_point_and_vector_addition(self):
        p = Point(3, 5)
        v = Vector(0, 1)

        p2 = p + v
        self.assertEqual(3, p2.x)
        self.assertEqual(6, p2.y)

    def test_two_point_addition(self):
        p1 = Point(3, 5)
        p2 = Point(0, 1)

        with self.assertRaises(TypeError) as context:
            p3 = p1 + p2


