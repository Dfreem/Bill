import random

import pygame.constants
from BillGame.states.base import BaseState
from BillGame.states.pieces.brick import Brick
from BillGame.states.pieces.cloud import Cloud
from BillGame.utility import __utility__


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

        # window
        self.bg_x = None
        self.bg_color = None
        self.bg_rect = None
        self.bg = None
        self.win_width = None
        self.win_height = None


        # game
        self.done = False
        self.next = 'main_menu'
        self.previous = 'main_menu'
        self.player = None
        self.window = None

        self.brick_frequency = None

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
        self.bg = pygame.image.load('images/bg.png').convert_alpha()
        self.bg = pygame.transform.smoothscale(self.bg, (self.win_width, self.win_height))
        self.bg_rect = self.bg.get_rect()
        self.bg_x = 0
        self.bg_color = self.bg.get_at((300, 300))
        self.bg.set_alpha(80)

        # # random generators
        # for _ in range(random.randint(10, 15)):
        #     self.clouds_rear.append(__utility__.rand_spot(Cloud(), window))
        # for _ in range(random.randint(10, 15)):
        #     self.bricks.append(__utility__.rand_spot(Brick(), window))
        # for _ in range(random.randint(10, 15)):
        #     self.clouds_front.append(__utility__.rand_spot(Cloud(True), window))

    def cleanup(self):
        pass

    def render_state(self, window, time_delta):
        """
            :type window: pygame.Surface
            :param window:
            :param time_delta:
            :return:
            """


    def get_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.rect.y -= self.player.vel_up

        if keys[pygame.K_UP]:
            self.player.rect.y += self.player.vel_up

    def on_run(self):
        pass

    def move_bricks(self, *bricks, speed=4):
        for item in bricks:
            if item.x >= -500:
                item.x -= speed
            else:
                item.x += self.win_width + 500
