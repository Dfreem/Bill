import sys

import pygame
from pygame import constants, K_p, K_DOWN, KEYUP, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, QUIT
from characters.bill import BulletBill
from pause import pause
from states.base import BaseState


class Game:
    def __init__(self, **settings):
        self.is_paused = False
        self.tick = None
        self.tick = 0.0

        self.state = None
        self.state_name = ""

        # player / character
        self._bill = BulletBill()

        self.window_size = (settings['win_width'], settings['win_width'])
        self.window = None
        self.settings = settings
        self.state: BaseState
        self.clock = pygame.time.Clock()

    def init(self):
        pygame.init()

        # setting up a game window
        self.window = pygame.display.set_mode(
            self.window_size,
            flags=pygame.constants.FULLSCREEN,
            display=1,
            vsync=1
        )

        # restricting events
        pygame.event.set_allowed([
            KEYDOWN,
            KEYUP,
            K_DOWN,
            K_p,
            K_ESCAPE,
            MOUSEBUTTONDOWN,
        ])

        self.window = pygame.display.set_mode(self.window_size).convert()
        self.window.fill(self.settings['sky_color'])
        self.state.state_setup(self._bill, self.window)
        self.state.done = False

    def setup_states(self, state_name, **states):
        """
        Called one time to transfer constructors and names as a dictionary

        :type state_name: str
        :param state_name:
        :type states: states.base.BaseState
        :param states: a dictionary of state object that inherit from BaseState
        :return: None
        """
        self.state = states[state_name]
        self.state_name = state_name

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
        The Game class' version of update first calls the states version,
        then passes the rects returned by state, to the display.
        update method.

         ... probably

        :return: None
        """
        returned_rects = self.state.render_state()
        pygame.display.update(returned_rects)

    def render(self):
        pass

    def main_loop(self):
        self.init()
        while not self.state.done:
            if not self.is_paused:

                self.tick = self.clock.tick(self.settings['fps']) / 1000.0

                for event in pygame.event.get():
                    self.process_events(event)
                pygame.event.pump()

                self.update()
                self.render()

    @property
    def game_window(self):
        return self.window

    @game_window.setter
    def game_window(self, value):
        """
        :type value: pygame.Surface
        :param value: a changed or initial copy / version of the game window
        :return: None
        """
        if value != self.window:
            value.convert()
            self.window = value

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

# import sys
# from abc import ABC, abstractmethod
# import pygame.event
# from pygame.constants import QUIT, K_p, KEYDOWN
# import pause
# from characters import bill
# from utility.bill_event import START_BUTTON
# from utility.manager import Manage
#
#     button_handler = Manage()
#     is_paused = False
#     window = None
#     character = None
#
#     def __init__(self, **settings):
#
#         # start pygame
#         pygame.init()
#
#     def setup_states(self, contexts, start_state):
#         self.contexts = contexts
#         self.state_name = start_state
#         self.state = self.contexts['main_menu']
#         self.state.state_setup(Game.character, self.window)
#
#
#     def update(self, delta_time):
#         """
#         call state_update method inside the current state,
#         then the button handlers draw_ui method
#
#         :param delta_time: clock.tick(fps) / 1000.0
#         :return: None
#         """
#         self.state.state_update(Game.window, delta_time)
#         # pygame.display.update(changed_rects)
#
#     def event_loop(self, delta_time):
#         """
#         Handle events in a separate loop than the game loop. here,
#         each event is passed off to the current state. The event and call are
#         perpetuated from each state to any buttons or sprites within.
#
#         :param delta_time: clock.tick(fps) / 1000.0
#         :return: None
#         """
#         events = pygame.event.get()
#         for event in events:
#             self.state.get_event(event)
#             # passing the event to the current state
#             if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE) :
#                 # click close button in corner of window
#                 pygame.quit()
#                 sys.exit()
#
#             if event.type == KEYDOWN:
#                 if event.key == K_p:
#                     self.is_paused = True
#
#             if event.type == START_BUTTON:
#                 self.flip_state()
#
#     def main_game_loop(self):
#         """
#         The only game loop controlling the flow of the game.
#         calls event_loop, update then display.update.
#
#         :return:
#         """
#         fps = self.__dict__['fps']
#         while not self.done:
#             if not self.is_paused:
#                 tick = self.clock.tick(fps)
#                 delta_time = tick / 1000.0
#                 self.event_loop(delta_time)
#                 self.update(self.window)
#                 Game.button_handler.draw_ui(Game.window)
#                 pygame.display.flip()
#             else:
#                 pygame.display.flip()
#                 pygame.event.clear()
#                 self.is_paused = pause.pause(self.is_paused, Game.window)
#
#