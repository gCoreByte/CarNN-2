import pygame as pyg
import os
import math
from ..util.util_game import vector_delta, Vector, Point


class Car(pyg.sprite.Sprite):
    """The car that the AI will drive, represented visually
    Returns: car object
    Functions: update, drive"""

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


    def update(self, turn, accelerate):
        self.drive(turn, accelerate)
        self.image = pyg.transform.rotate(self.image_base, math.degrees(self.vector.angle))
        self.rect = self.image.get_rect(center = self.rect.center)

    def drive(self, turn, accelerate):

        # variables
        friction = 0.04
        angular_speed = 1


        # turning
        if turn == 1:
            self.vector.angle -= math.radians(angular_speed)
        elif turn == -1:
            self.vector.angle += math.radians(angular_speed)

        self.vector.z = accelerate

        # finding new x, y axis acceleration
        speed_x, speed_y = vector_delta(self.vector)
        self.speed_x += speed_x
        self.speed_y += speed_y

        # applying friction
        # if speed is bigger than ~0, we apply friction
        #if self.speed_x > 0.01 or self.speed_x < -0.01:
        self.speed_x = self.speed_x - self.speed_x * friction
        #if self.speed_y > 0.01 or self.speed_y < -0.01:
        self.speed_y = self.speed_y - self.speed_y * friction

        # moving the rectangle
        self.rect.move_ip((self.speed_x, self.speed_y))
