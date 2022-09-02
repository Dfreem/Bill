import random

import pygame
from pygame import rect
from pygame.sprite import Sprite


class Brick(Sprite):
    cloud_count = 0
    brick_count = 0
    _filepath = "images/mario_items.png"

    def __init__(self):
        super(Brick, self).__init__()
        # stats
        self.size = None
        self.y = 0
        self.x = 0
        self.width = 16
        self.height = 16
        self._hp = 10
        self._is_breakable = True
        self._is_broken = False
        self._damage = 0
        self.window = None
        self.win_size = pygame.display.get_window_size()

        # ------ self identity / shape ------
        self.filepath = 'images/mario_items.png'
        self.image = pygame.image.load(self.filepath).convert_alpha()
        self.image = pygame.Surface.subsurface(self.image, [0, 0], [self.width, self.height]).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (30, 30))
        self.rect = self.image.get_rect()

    @property
    def hp(self):
        return self.hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def is_breakable(self):
        return "breakable: " + str(self._is_breakable) + "\nis broken: " + str(self._is_broken)

    @is_breakable.setter
    def is_breakable(self, value):
        if type(value) == bool:
            self._is_breakable = value

    def get_smashed(self):
        self.kill()

    def take_damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.get_smashed()
