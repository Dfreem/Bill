import pygame.display

import BillGame
from BillGame import game
from BillGame.states.base import BaseState
from BillGame.utility import bill_event
from BillGame.utility.__utility__ import create_button
from BillGame.utility.bill_event import LEVEL_BUTTON


class MainMenu(BaseState):

    def __init__(self):
        super(MainMenu, self).__init__()
        self.done = False
        self.quit = False
        self.next = "level_rand"
        self.previous = None
        self.state_name = "main_menu"
        self.start_button = None
        self.level_button = None
        self.background = None

    def state_setup(self, player, window):

        # building menu buttons
        # start
        self.start_button = create_button(
            y=2
        )
        self.start_button.set_event(bill_event.START_BUTTON)

        # adding them to the game ui container
        game.Game.ui_container.add(self.start_button)

        # level select
        self.level_button = create_button(
            'images/editor_btn.png',
            y=2, x=2
        )
        self.level_button.set_event(LEVEL_BUTTON)
        game.Game.ui_container.add(self.level_button)
        self.background = pygame.image.load('images/start_screen.png').convert()
        window.blit(self.background, (0, 0))

        # window.blit(self.start_button, self.start_button.rect)
        # window.blit(self.level_button, self.level_button.rect)

    def on_run(self, window):
        pass

    def get_event(self, event):
        self.start_button.get_event(event)
        if event.type == bill_event.START_BUTTON:
            print("ahhhhhh")
            self.done = True

    def cleanup(self):
        game.Game.ui_container.empty()

    def render_state(self, window):
        window.blit(self.background, (0, 0))
        game.Game.ui_container.draw(window)

    def update(self, window):
        pass
