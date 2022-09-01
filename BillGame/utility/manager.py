import pygame.sprite

from game import Game
from states.menu import MainMenu
from states.random_level import LevelRand


class UIManager:
    ui_container = pygame.sprite.OrderedUpdates()

    def draw_ui(self, window):
        """
        :type window: pygame.Surface
        :param window: the Game window.
        :return: a list of rectangles that have been changed.
         these should be passed to display update
        """
        return self.ui_container.draw(window)


class StateManager:
    contexts = {
        "main_menu": MainMenu(),
        "level_rand": LevelRand(),
    }

    def __init__(self, game):
        game.setup_states(self.contexts)
        self.state = game.state = self.contexts['main_menu']
        game.main_loop()

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

        print("flipping states from: " + repr(self.state))

        previous, self.state.state_name = self.state.state_name, self.state.next
        self.state.is_paused = False
        self.state = self.contexts[self.state.state_name]
        print("to: " + repr(self.state))
        self.state.state_setup(self.state, self.state.window)
        self.state.on_run()
        self.state.previous = previous