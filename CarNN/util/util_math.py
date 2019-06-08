"""In this file are general math functions to
improve usability and readability of the code."""


import math


class Vector:
    """A simple vector wrapper
    Returns: Vector object
    Attributes: angle, z"""
    def __init__(self, angle, z):
        self.angle = angle
        self.z = z


class Point:
    """A simple point wrapper
    Returns: Point object
    Attributes: x, y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    """A simple line wrapper
    Returns: Line object
    Attributes: Point 1, Point 2"""
    def __init__(self, point_1 : Point, point_2 : Point):
        self.point_1 = point_1
        self.point_2 = point_2


def vector_delta(vector  : Vector):
    """
    Function, which takes in a Vector and returns the delta_x and delta_y
    :param vector: Vector class
    :return: -delta_x, -delta_y
    :rtype float, float
    """
    (delta_x, delta_y) = (vector.z * math.sin(vector.angle), vector.z * math.cos(vector.angle))
    return -delta_x, -delta_y


def rotate_point(point : Point, angle, pivot : Point):
    """
    Function, which rotates a point around a pivot by a certain angle
    :param point: point to rotate
    :param angle: angle to rotate by
    :param pivot: point to rotate around
    :return: rotated point
    """
    # translating point back to origin
    point.x -= pivot.x
    point.y -= pivot.y

    # rotating point
    point.x = point.x * math.cos(angle) - point.y * math.sin(angle)
    point.y = point.x * math.sin(angle) + point.y * math.cos(angle)

    # translate point back
    point.x += pivot.x
    point.y += pivot.y
    return point


def line_intersection(line1 : Line, line2 : Line):
    """
    Function, which returns if a line segment intersects another
    :param line1: Line 1
    :param line2: Line 2
    :return: False if lines do not intersect, otherwise True
    """
    xdiff = (line1.point_1.x - line1.point_2.x, line2.point_1.x - line2.point_2.x)
    ydiff = (line1.point_1.y - line1.point_2.y, line2.point_1.y - line2.point_2.y)

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    div = det(xdiff, ydiff)
    if div == 0:
        return False
    else:
        return True
    """
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y
    """
