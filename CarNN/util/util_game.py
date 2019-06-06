"""In this file are general utility functions
and additions to the Pygame library, such as simplified
vector calculations"""

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

def vector_delta(vector):
    """
    Function, which takes in a Vector and returns the delta_x and delta_y
    :param vector: Vector class
    :return: -delta_x, -delta_y
    :rtype float, float
    """
    (delta_x, delta_y) = (vector.z * math.sin(vector.angle), vector.z * math.cos(vector.angle))
    return -delta_x, -delta_y


def rotate_point(point, angle, pivot):
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
