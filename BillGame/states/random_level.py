import random

import pygame.constants

from game import Game, BaseState
from states.pieces.brick import Brick
from states.pieces.cloud import Cloud


def gain_speed(v):
    """
    increases velocity passed in as v by %10 as long as v is <= 15
    :type v: int
    :param v: velocity
    :return: new velocity
    """
    if v <= 15:
        v *= 1.1
    return v


class LevelRand(BaseState):
    """
    Randomly generated level for bill

    """

    bricks = []
    clouds_rear = []
    clouds_front = []

    def __init__(self):
        super(LevelRand, self).__init__()

        # background
        self.bg = pygame.image.load('images/bg.png').convert_alpha()
        pygame.transform.smoothscale(self.bg, (1200, 600))
        self.bg_rect = self.bg.get_rect()
        self.bg.set_alpha(80)

        # window
        self.win_width = None
        self.win_height = None

        # game
        self.next = 'main_menu'
        self.previous = 'main_menu'
        self.player = None
        self.window = None

    def state_setup(self, player, window):
        """
        override to notify this state that it will be switched to soon.

        :type player: pygame.sprite.Sprite
        :param player: the player character (bullet bill)
        :type window: pygame.Surface
        :param window: The Game window
        :return: None
        """
        self.player = player
        self.window = window

        self.win_width = window.get_width()
        self.win_height = window.get_height()

        # random generators
        for _ in range(random.randint(10, 15)):
            Brick().rand_spot(LevelRand.bricks)
        for _ in range(random.randint(10, 15)):
            Cloud().rand_spot(LevelRand.clouds_rear)
        for _ in range(random.randint(10, 15)):
            Cloud(True).rand_spot(LevelRand.clouds_front)

    def cleanup(self):
        pass

    def render_state(self, window, time_delta):
        """
        :type window: pygame.Surface
        :param window:
        :param time_delta:
        :return:
        """

        window.fill(pygame.Color('#B4D0F0'))
        window.blit(self.bg, (self.bg_rect.x, self.bg_rect.y))
        window.blit(self.bg, (self.bg_rect.x + self.bg_rect.width, self.bg_rect.y))
        self.bricks = move_bricks(self.bricks)
        self.clouds_rear = move_bricks(self.clouds_rear, 3)
        self.clouds_front = move_bricks(self.clouds_front, 5)
        window.blits(self.clouds_rear)
        window.blits(self.bricks)
        window.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        window.blits(self.clouds_front)

    def get_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.rect.y -= self.player.vel_up

        if keys[pygame.K_UP]:
            self.player.rect.y += self.player.vel_up
        self.character.draw(Game.window)

    def on_run(self):
        self.window.blits([self.bg, (0, 0), (self.bg, (1000, 0))])
        # self.window.blit(self.bg, (1000, 0))
        self.window.blits(self.bricks)
        self.window.blits(self.clouds_rear)
        self.window.blit(self.player.image, self.player.rect)

def move_bricks(bricks, speed=4):
    holder = []
    for i in range(len(bricks)):
        img, rct = bricks[i]
        if rct.x > -600:
            rct.x -= speed
        else:
            rct.x += self.window.get_width() * 2
        holder.append((img, rct))
    return holder




