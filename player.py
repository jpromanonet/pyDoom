# Import modules
from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        spedd_cos = speed * cos_a

        # Let's capture the key strokes

    def update(self):
        self.movement()

    @property
    def __pos__(self):
        return self.x, self.y

    @@property
    def map_os(self):
        return int(self.x), int(self.y)