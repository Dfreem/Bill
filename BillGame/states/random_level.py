import random
import pygame.constants
from characters.bill import BulletBill
from states.base import BaseState
from states.pieces.brick import Brick
from states.pieces.cloud import Cloud
from utility import __utility__, bill_event


class LevelRand(BaseState):
    """
    Randomly generated level for bill

    """
    # holding lists for level items
    bricks = []
    clouds_rear = []
    clouds_front = []
    all = []

    def __init__(self):
        super(LevelRand, self).__init__()

        # level
        self.player = None
        self.player: BulletBill

        # window
        self.bg_color = None
        self.bg = None
        self.win_width = None
        self.win_height = None
        self.window = None
        # self.bg_x = None
        # self.bg_rect = None

        # game
        self.done = False
        self.next = 'main_menu'
        self.previous = 'main_menu'

    def state_setup(self, player, window):
        """
        override to notify this state that it will be switched to soon.

        :type player: characters.bill.BulletBill
        :param player: the player character (bullet bill)
        :type window: pygame.Surface
        :param window: The Game window
        :return: None
        """
        # transfer of player and window
        self.player: BulletBill = player
        self.window: pygame.Surface = window
        self.win_width = window.get_width()
        self.win_height = window.get_height()

        # loading background picture
        self.bg = pygame.image.load('images/bg.png').convert_alpha()

        # resizing to the size of the window
        self.bg = pygame.transform.smoothscale(self.bg, (self.win_width, self.win_height))

        # save the color that already being used for the background
        self.bg_color = self.bg.get_at((300, 300))

        # making the background a little transparent
        self.bg.set_alpha(80)
        # self.bg_rect = self.bg.get_rect()

        # random generators
        # first is clouds in the background
        for _ in range(random.randint(10, 15)):

            # this is broken down in order to change the scroll speed from the default.
            temp_cloud = Cloud()
            temp_cloud.scroll = 2
            self.clouds_rear.append(__utility__.rand_spot(temp_cloud, window))

        # Generating brick-blocks
        for _ in range(random.randint(10, 15)):

            # the scroll speed is set with these blocks in mind, so they get the default
            self.bricks.append(__utility__.rand_spot(Brick(), window))

        # the clouds in the foreground get enlarged and the alpha increased by setting foreground to True
        for _ in range(random.randint(10, 15)):
            another_cloud = Cloud(foreground=True)

            # faster scroll speed
            another_cloud.scroll = 5
            self.clouds_front.append(__utility__.rand_spot(another_cloud, window))

    def cleanup(self):
        """
        Is called when a level is done

        :return: None
        """
        self.bricks.clear()
        self.clouds_front.clear()
        self.clouds_rear.clear()
        self.window.fill(self.bg_color)

    def render_state(self, window):
        """
        is called every frame to draw level items to the screen

        :type window: pygame.Surface
        :param window: the game window
        """

        window.blit(self.bg, (0, 0))

        # iterating through as list to draw each item.
        # in order: background clouds, bricks, foreground clouds.
        for cloud in self.clouds_rear:
            window.blit(cloud.image, cloud.rect)
        for box in self.bricks:
            window.blit(box.image, box.rect)
        for thing in self.clouds_front:
            window.blit(thing.image, thing. rect)
        window.blit(self.player.image, self.player.rect)

    def get_event(self, event):
        """
        Called when an allowed event is put on the stack
        :param event:
        :return:
        """
        if event.type == bill_event.BRICK_HIT:
            print(event)

    def on_run(self, window):
        self.all.extend(self.bricks)
        self.all.append(self.player)

    def update(self, window):
        for cloud in self.clouds_rear:
            cloud.update()
        for block in self.bricks:
            block.update()
        for thing in self.clouds_front:
            thing.update()
        self.get_keys()
        self.check_bricks()
        self.check_player()

    def get_keys(self):
        """
        get the keyboard specific events during this state's gameplay.
        :return: None
        """
        keys = pygame.key.get_pressed()

        # move player up
        if keys[pygame.K_UP]:
            self.player.y_coord -= self.player.vel_up
            if self.player.vel_up < 8:
                self.player.vel_up += 0.5
        else:
            self.player.vel_up = BulletBill.bill_vel
        if keys[pygame.K_DOWN]:
            self.player.y_coord += self.player.vel_down
            if self.player.vel_down < 8:
                self.player.vel_down += 0.5
        else:
            self.player.vel_down = BulletBill.bill_vel

        if self.player.y_coord < 0:
            self.player.y_coord += self.win_height + 100

        if self.player.y_coord > self.win_height:
            self.player.y_coord -= self.win_height + 100

    def check_bricks(self):
        for a_brick in self.bricks:
            if a_brick.rect.colliderect(self.player.rect):
                a_brick.take_damage(self.player.damage)
            if a_brick.is_broken:
                self.kill_brick(a_brick)

    def check_player(self):

        if self.player.rect.collidelist(self.bricks) > 0:

            # tying to break this down for readability

            # retrieve the index in the list of bricks of the hit brick.
            bricks_house = self.player.rect.collidelist(self.bricks)

            # retrieving the brick in the specified location
            the_brick_that_hit = self.bricks[bricks_house]

            # applying the damage to the player
            self.player.take_damage(the_brick_that_hit.damage)

    def kill_brick(self, brick):
        brick.image = brick.breaking1
        if brick.death_timer < 450:
            try:
                exec(next(brick.exploding))
            except StopIteration:
                transparent = brick.image.get_at((0, 0))
                brick.image.set_alpha(transparent)
                brick.image.fill(transparent)
            finally:
                self.window.blit(brick.image, brick.rect)

