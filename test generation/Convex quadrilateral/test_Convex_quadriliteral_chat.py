import unittest
from Convex_quadrilateral import four_lines_area, lines_intersection, distance, quadrangle_area

# test_convex_quadrilateral_area.py

class TestConvexQuadrilateralArea(unittest.TestCase):

    def test_lines_intersection_parallel(self): # OK
        self.assertIsNone(lines_intersection(1, 0, 1, 1))  # Parallel lines

    def test_lines_intersection_coinciding(self): #mistake, should be none
        self.assertEqual(lines_intersection(1, 0, 1, 0), (0.0, 0.0))  # Coinciding lines

    def test_lines_intersection_normal(self): # OK
        self.assertEqual(lines_intersection(1, 0, -1, 2), (1.0, 1.0))

    def test_distance(self):
        self.assertEqual(distance(0, 0, 3, 4), 5.0) # OK
        self.assertAlmostEqual(distance(-1, -1, 2, 2), 5.66, places=2) # wrong, shold be sqrt(18), 4,24

    def test_quadrangle_area_valid(self): # OK
        self.assertEqual(quadrangle_area(3, 4, 3, 4, 5, 5), 12.0)

    def test_quadrangle_area_invalid(self): # OK
        self.assertIsNone(quadrangle_area(1, 1, 1, 1, 2, 2))

    def test_four_lines_area_valid(self): # should be 0,5
        self.assertEqual(four_lines_area(1, 0, -1, 0, 1, 1, -1, 1), 4.0)

    def test_four_lines_area_zero(self): # OK
        self.assertEqual(four_lines_area(1, 0, 1, 0, 1, 1, 1, 2), 0)

    def test_four_lines_area_no_quadrilateral(self):
        self.assertEqual(four_lines_area(1, 0, 1, 1, 1, 2, 1, 3), 0)
        self.assertEqual(four_lines_area(1, 0, -1, 0, 1, 1, -1, 1), 0) # should be 0,5

if __name__ == '__main__':
    unittest.main()
