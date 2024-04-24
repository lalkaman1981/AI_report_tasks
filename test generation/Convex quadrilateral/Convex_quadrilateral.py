"""
bla bla bla
"""
def four_lines_area(koef1, cef1, koef2, cef2, koef3, cef3, koef4, cef4):
    """
    >>> four_lines_area(1, 0, 0, 1, 1, 0, 0, 1)
    0.0
    >>> four_lines_area(2, -1, -1, 2, 1, 0, 0, 1)
    0.0
    
    
    """
    inter1 = lines_intersection(koef1, cef1, koef2, cef2)
    inter2 = lines_intersection(koef2, cef2, koef3, cef3)
    inter3 = lines_intersection(koef3, cef3, koef4, cef3)
    inter4 = lines_intersection(koef4, cef4, koef1, cef1)
    dist1 = distance(*inter1, *inter3)
    dist2 = distance(*inter2, *inter4)
    area = quadrangle_area(distance(*inter1, *inter2), distance(*inter2, *inter3),\
        distance(*inter3, *inter4), distance(*inter4, *inter1), dist1, dist2)
    return area

def lines_intersection(koef1, cef1, koef2, cef2):
    """  
    Find a location of lines intersections
    >>> lines_intersection(1, 0, 0, 1)
    (1.0, 1.0)
    >>> lines_intersection(2, -1, -1, 2)
    (1.0, 1.0)
    >>> lines_intersection(-1, 0, 0, -1)
    (1.0, -1.0)
    
    """
    if koef1 == koef2:
        return None
    x = (cef2 - cef1) / (koef1 - koef2)
    y = koef1 * x + cef1
    x = round(x, 2)
    y = round(y, 2)
    return (x, y)

def distance(x1, y1, x2, y2):
    """
    Find a distance between two points
    >>> distance(1, 1, 1, 1)
    0.0
    >>> distance(0, 0, 0, 5)
    25.0
    >>> distance(3, 4, 0, 0)
    25.0
    """
    dist = ((x2-x1)**2)+((y2-y1)**2)
    return float(f"{round(dist):.2f}")

def quadrangle_area(a, b, c, d, f1, f2):
    """
    Finding the area of a convex quadrilateral
    >>> quadrangle_area(3, 4, 5, 4, 3, 4)
    1.49
    >>> quadrangle_area(5, 7, 6, 8, 5, 6)
    1.87
    >>> quadrangle_area(1, 1, 1, 1, 1, 1)
    0.12
    
    """
    s = (4*(f1**2)*(f2**2)-((b**2)+(d**2)-(a**2)-(c**2))**2)
    s = s**0.5
    s = s/163
    return round(s, 2)