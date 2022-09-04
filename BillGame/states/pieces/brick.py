import asyncio

import pygame
from pygame.time import wait

from states.pieces.cloud import Cloud
from utility import bill_event


class Brick(Cloud):
    _filepath = "images/mario_items.png"

    def __init__(self):
        """
        This class represents the bricks on screen. It inherits from Cloud who ultimately inherits from Sprite.
        Added to the functionality of Cloud, is a breaking mechanism. It can be set to be non-breakable, deal more damage and
        adjust scroll-speed.

         this class is sub-class-able further for any game object that requires these attributes,
         such as enemies or any breakable objects.
        """
        super(Brick, self).__init__()

        # stats
        # rect
        self.y = 0
        self.x = 0
        self.width = 16
        self.height = 16

        # interactions
        self._hp = 10
        self._is_breakable = True
        self.is_broken = False
        self.scroll_speed = 5
        self.death_timer = 0

        # how much damage it deals when interacting
        self.damage = 0
        self.win_size = pygame.display.get_window_size()

        # ------ self identity / shape ------
        self.filepath = 'images/mario_items.png'
        self.original = pygame.image.load(self.filepath).convert_alpha()
        self.image = pygame.Surface.subsurface(self.original, [0, 0], [self.width, self.height]).convert_alpha()
        self.breaking1 = pygame.image.load("images/exploding_brick1.png").convert_alpha()
        self.breaking2 = pygame.image.load("images/exploding_brick2.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        explode_sequence = [
            "self.image.blit(self.breaking1, (0, 0))",
            "self.image.blit(self.breaking2, (0, 0))",
            "self.is_broken = True"
        ]
        self.exploding = iter(explode_sequence)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def is_breakable(self):
        return "breakable: " + str(self._is_breakable) + "\nis broken: " + str(self.is_broken)

    @is_breakable.setter
    def is_breakable(self, value):
        if type(value) == bool:
            self._is_breakable = value

    def get_smashed(self):
        if self.is_breakable:
            self.rect.width = 0
            self.rect.height = 0
            # self.death()
            self.kill()

    def take_damage(self, value):
        if not self.is_broken:
            self.hp -= value
            if self.hp <= 0:
                self.get_smashed()

    # stopped here, 09/03/22
    # def death(self):
    #     for event in pygame.event.get():
    #         print(self.death_timer)
    #         if event.type == bill_event.COUNT_THIS:
    #             self.death_timer += 1
    #         if self.death_timer == 500:
    #             exec(next(self.exploding))


