import sys

import pygame
from pygame import constants, K_p, KEYUP, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, QUIT, sprite

from characters.bill import BulletBill
from pause import pause
from utility import __utility__
from utility.bill_event import START_BUTTON, LEVEL_BUTTON


class Game:
    ui_container = sprite.OrderedUpdates()
    bg_container = sprite.OrderedUpdates()
    bricks = sprite.Group()
    clouds = sprite.LayeredUpdates()

    def __init__(self, **settings):
        pygame.init()
        self.tick = None
        self.state = None
        self.state_name = ""
        self.states = None
        self.done = False
        self.is_paused = False
        self.settings = settings

        self.clock = pygame.time.Clock()
        self.window_size = (settings['win_width'], settings['win_height'])

        # restricting events
        pygame.event.set_allowed([
            KEYDOWN,
            KEYUP,
            START_BUTTON,
            LEVEL_BUTTON,
            MOUSEBUTTONDOWN,
        ])

        # setting up a game window
        self.window = pygame.display.set_mode(
            self.window_size,
            depth=32,
            flags=constants.NOFRAME
        )
        self.window.convert()

        # player / character
        self._bill = BulletBill()

    @property
    def get_settings(self):
        return self.settings

    @get_settings.setter
    def get_settings(self, value):
        pass

    @property
    def get_bill(self):
        return self._bill

    @get_bill.setter
    def get_bill(self, value):
        self._bill = value

    def setup_states(self, start_state, **states):
        """
        Called one time to transfer constructors and names as a dictionary

        :type start_state: str
        :param start_state: which state to start on
        :param states: a dictionary of state object that inherit from BaseState
        :return: None
        """
        self.states = states
        self.state = states[start_state]
        self.state_name = start_state
        self.window.fill(self.settings['sky_color'])
        self.state.state_setup(self._bill, self.window)
        self.state.done = False

    def process_events(self, event):
        self.state.get_event(event)
        if event.type == KEYDOWN:
            if event.key == K_p:
                pause(self.is_paused, self.window)
            if event.key == K_ESCAPE or event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

    def update(self):
        """
        call all the game components update methods

        :return: None
        """
        # erase contents and start a fresh screen. called once a frame.
        self.window.fill(self.settings['sky_color'])

        # update the currently loaded state
        self.state.update(self.window)

        # demand that the state draw itself.
        # We won't be pushed around by a state we don't even kow the name of ...
        self.state.render_state(self.window)

        # onscreen debugger w/ hp and FPS info
        self.window.blit(__utility__.update_fps(self.clock.get_fps(), self._bill.hp), (50, 50))
        pygame.display.update()

    def main_loop(self):
        self.state.done = False
        while not self.done:
            if not self.is_paused and not self.state.done:

                self.tick = self.clock.tick(self.settings['fps']) / 1000.0

                for event in pygame.event.get():
                    self.process_events(event)
                pygame.event.pump()

                self.update()
            else:
                self.flip_state()

    def flip_state(self):
        """
        switch current state to next state

        :return: None

        switcheroo automatically, simultaneously swaps
        the current string name of the state w/ -> previous state position
                                    - and -
        next state position w/ -> current string state name"""

        self.state.done = False
        self.state.cleanup()

        print("flipping states from: " + repr(self))

        previous, self.state_name = self.state_name, self.state.next
        self.is_paused = False
        self.state.cleanup()
        self.state = self.states[self.state_name]
        print("to: " + repr(self))
        self.state.state_setup(self.get_bill, self.window)
        self.state.on_run(self.window)
        self.state.previous = previous
        # self.main_loop()
