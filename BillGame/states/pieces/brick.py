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
        self.y = None
        self.x = None
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

    def rand_spot(self, handler):

        self.x = random.randint(-500, self.win_size[0] * 2)
        self.y = random.randint(0, self.win_size[1])
        self.rect = rect.Rect((self.x, self.y), (16, 16))
        handler.append((self.image, self.rect))

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
        pass

    def take_damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.get_smashed()
