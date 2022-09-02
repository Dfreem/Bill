import sys
import pygame
from pygame import constants, K_p, K_DOWN, KEYUP, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, QUIT, sprite
from BillGame.utility import bill_event
from BillGame.utility.bill_event import START_BUTTON, LEVEL_BUTTON
from characters.bill import BulletBill
from pause import pause


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
            flags=constants.NOFRAME,
            vsync=1
        )

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

    def update(self, time_delta):
        """
        The Game class' version of update first calls the states version,
        then passes the rects returned by state, to the display.
        update method.

         ... probably

        :return: None
        """
        self.window.fill(self.settings['sky_color'])

        self.state.render_state(self.window, time_delta)

        pygame.display.update()

    def main_loop(self):
        self.state.done = False
        while not self.state.done:
            if not self.is_paused:

                self.tick = self.clock.tick(self.settings['fps']) / 1000.0

                for event in pygame.event.get():
                    self.process_events(event)
                pygame.event.pump()

                self.update(self.tick)
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
        self.state = self.states[self.state_name]
        self.state.cleanup()
        print("to: " + repr(self))
        self.state.state_setup(self.get_bill, self.window)
        self.state.on_run()
        self.state.previous = previous
        self.main_loop()

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