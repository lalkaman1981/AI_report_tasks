import unittest
from Convex_correct import four_lines_area, lines_intersection, distance, quadrangle_area

# test_convex_quadrilateral_area.py


class TestConvexQuadrilateralArea(unittest.TestCase):

    def test_lines_intersection_parallel(self):
        self.assertIsNone(lines_intersection(1, 0, 1, 1))  # Parallel lines

    def test_lines_intersection_coinciding(self):
        self.assertIsNone(lines_intersection(1, 0, 1, 0))  # Coinciding lines

    def test_lines_intersection_normal(self):
        self.assertEqual(lines_intersection(1, 0, -1, 2), (1.0, 1.0))

    def test_distance(self):
        self.assertEqual(distance(0, 0, 3, 4), 5.0)
        self.assertAlmostEqual(distance(-1, -1, 2, 2), 4.24, places=2)

    def test_quadrangle_area_valid(self):
        self.assertEqual(quadrangle_area(3, 4, 3, 4, 5, 5), 12.0)

    def test_quadrangle_area_invalid(self):
        self.assertIsNone(quadrangle_area(1, 1, 1, 1, 2, 2))

    def test_four_lines_area_valid(self):
        self.assertAlmostEqual(four_lines_area(1, 0, -1, 0, 1, 1, -1, 1), 0)

    def test_four_lines_area_zero(self):
        self.assertEqual(four_lines_area(1, 0, 1, 0, 1, 1, 1, 2), 0)

    def test_four_lines_area_no_quadrilateral(self):
        self.assertEqual(four_lines_area(1, 0, 1, 1, 1, 2, 1, 3), 0)
        self.assertEqual(four_lines_area(1, 0, -1, 0, 1, 1, -1, 1), 0)

if __name__ == '__main__':
    unittest.main()
