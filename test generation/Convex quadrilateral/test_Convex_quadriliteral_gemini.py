import unittest
from Convex_correct import four_lines_area, lines_intersection, distance, quadrangle_area

# test_convex_quadrilateral_area.py


class TestConvexQuadrilateralArea(unittest.TestCase):
    def test_lines_intersection_basic(self):
        self.assertEqual(lines_intersection(1, 2, 2, -1), (3.0, 5.0))

    def test_lines_intersection_non_integer(self):
        self.assertEqual(lines_intersection(0.5, 1, -1, 3), (1.33, 1.67))

    def test_lines_intersection_parallel(self):
        self.assertIsNone(lines_intersection(2, 1, 2, -3))

    def test_lines_intersection_coincident(self):
        self.assertIsNone(lines_intersection(1, 2, 1, 2))
    
    def test_distance_basic(self):
        self.assertEqual(distance(1, 1, 4, 5), 5.0)

    def test_distance_negative_coordinates(self):
        self.assertEqual(distance(-2, 3, 1, -1), 5.0) 

    def test_distance_same_point(self):
        self.assertEqual(distance(3, 2, 3, 2), 0.0)
    
    def test_quadrangle_area_valid(self):
        self.assertEqual(quadrangle_area(3, 4, 2, 5, 5, 4), 7.14)

    def test_quadrangle_area_invalid(self):
        self.assertIsNone(quadrangle_area(1, 2, 3, 4, 1, 1))  # Not a valid quadrilateral


    def test_four_lines_no_quadrilateral(self):
        self.assertEqual(four_lines_area(1, 0, 1, 2, 1, 4, 2, 0), 0.0)  # Three parallel lines


if __name__ == '__main__':
    unittest.main()
