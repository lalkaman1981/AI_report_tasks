import unittest
from Convex_quadrilateral import four_lines_area, lines_intersection, distance, quadrangle_area


def test_lines_intersection():
    assert lines_intersection(1, 0, 1, 1) is None  # Parallel lines
    assert lines_intersection(1, 0, 1, 0) == (0.0, 0.0)  # Coinciding lines
    assert lines_intersection(1, 0, -1, 2) == (1.0, 1.0)

def test_distance():
    assert distance(0, 0, 3, 4) == 5.0
    assert distance(-1, -1, 2, 2) == 5.66

def test_quadrangle_area():
    assert quadrangle_area(3, 4, 3, 4, 5, 5) == 12.0
    assert quadrangle_area(1, 1, 1, 1, 2, 2) is None

def test_four_lines_area():
    assert four_lines_area(1, 0, -1, 0, 1, 1, -1, 1) == 4.0
    assert four_lines_area(1, 0, 1, 0, 1, 1, 1, 2) == 0
    assert four_lines_area(1, 0, 1, 1, 1, 2, 1, 3) == 0
    assert four_lines_area(1, 0, -1, 0, 1, 1, -1, 1) == 0

if __name__ == "__main__":
    test_lines_intersection()
    test_distance()
    test_quadrangle_area()
    test_four_lines_area()
    print("All tests passed.")