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
        pass

    def update(self):
        self.movement()

    @property
    def __pos__(self):
        return self.x, self.y

    @@property
    def map_os(self):
        return int(self.x), int(self.y)