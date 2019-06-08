import pygame as pyg
from enum import IntEnum
from ..util.util_math import Line, Point


class BlockType(IntEnum):
    LeftRight = 0
    UpDown = 1
    BottomLeftTopRight = 2
    BottomRightTopLeft = 3


class Direction:
    def __init__(self, x_move, y_move, x_width, y_width):
        self.x_move = x_move
        self.y_move = y_move
        self.x_width = x_width
        self.y_width = y_width


Up = Direction(0, -270, 90, 0)
Down = Direction(0, 270, -90, 0)
Left = Direction(-270, 0, 0, -90)
Right = Direction(270, 0, 0, 90)

current_direction = Right

