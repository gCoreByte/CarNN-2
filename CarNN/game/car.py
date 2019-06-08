import pygame as pyg
import os
import math
from ..util.util_math import vector_delta, rotate_point, line_intersection, Vector, Point, Line


class Car(pyg.sprite.Sprite):
    """The car that the AI will drive, represented visually
    Returns: car object
    Functions: update, drive, have_crashed"""

    def __init__(self, x, y, angle):
        pyg.sprite.Sprite.__init__(self)
        self.image_base = pyg.image.load(os.path.join('.', 'res', 'car.png')).convert()
        self.image_base.set_colorkey((0, 0, 0))
        self.image = self.image_base
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # physics variables
        self.vector = Vector(angle, 0)
        self.speed_x = 0
        self.speed_y = 0

        # collision variables
        self.corners = [Point(self.rect.bottomleft[0], self.rect.bottomleft[1]),
                        Point(self.rect.bottomright[0], self.rect.bottomright[1]),
                        Point(self.rect.topright[0], self.rect.topright[1]),
                        Point(self.rect.topleft[0], self.rect.topleft[1])]

    def update(self, turn, accelerate, map_guide):
        self.drive(turn, accelerate)
        self.have_crashed(map_guide)
        self.image = pyg.transform.rotate(self.image_base, math.degrees(self.vector.angle))
        self.rect = self.image.get_rect(center = self.rect.center)

    def drive(self, turn, accelerate):

        # variables
        new_corners = self.corners
        friction = 0.04
        angular_speed = math.radians(1)


        # turning
        if turn == 1:
            self.vector.angle -= angular_speed
            new_corners = []
            for i in self.corners:
                new_corners.append(rotate_point(i, -angular_speed, self.rect.center))
        elif turn == -1:
            self.vector.angle += angular_speed
            new_corners = []
            for i in self.corners:
                new_corners.append(rotate_point(i, angular_speed, self.rect.center))

        self.vector.z = accelerate

        # finding new x, y axis acceleration
        speed_x, speed_y = vector_delta(self.vector)
        self.speed_x += speed_x
        self.speed_y += speed_y

        # applying friction
        # if speed is bigger than ~0, we apply friction
        # if self.speed_x > 0.01 or self.speed_x < -0.01:
        self.speed_x = self.speed_x - self.speed_x * friction
        # if self.speed_y > 0.01 or self.speed_y < -0.01:
        self.speed_y = self.speed_y - self.speed_y * friction

        self.corners = []

        # moving the rectangle, adjusting corners
        for corner in new_corners:
            self.corners.append(Point(i.x + speed_x, i.y + speed_y))
        self.rect.move_ip((self.speed_x, self.speed_y))

    def have_crashed(self, map_guide):
        # finding sides of rectangle for collision
        collision_lines = [Line(self.corners[0], self.corners[1]),
                           Line(self.corners[1], self.corners[2]),
                           Line(self.corners[2], self.corners[3]),
                           Line(self.corners[3], self.corners[0])]

        for line in map_guide:
            for side in collision_lines:
                if line_intersection(line, side):
                    return True
        return False

