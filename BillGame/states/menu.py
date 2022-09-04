import pygame.display
from game import Game
from states.base import BaseState
from utility import bill_event
from utility.__utility__ import create_button
from utility.bill_event import START_BUTTON, LEVEL_BUTTON


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
        Game.ui_container.add(self.start_button)

        # level select
        self.level_button = create_button(
            'images/editor_btn.png',
            y=2, x=2
        )
        self.level_button.set_event(LEVEL_BUTTON)
        Game.ui_container.add(self.level_button)
        self.background = pygame.image.load('images/start_screen.png').convert()
        window.blit(self.background, (0, 0))

        # window.blit(self.start_button, self.start_button.rect)
        # window.blit(self.level_button, self.level_button.rect)

    def on_run(self):
        pass

    def get_event(self, event):
        self.start_button.get_event(event)
        if event.type == bill_event.START_BUTTON:
            print("ahhhhhh")
            self.done = True

    def cleanup(self):
        Game.ui_container.empty()

    def render_state(self, window):
        window.blit(self.background, (0, 0))
        Game.ui_container.draw(window)

    def update(self, window):
        pass
#
# def create_button(filepath=None, x=None, y=None, parent_func='print("not implemented in menu")'):
#     """
#     Create specialized buttons for the main menu.
#     x and y are optional. if both are None, placement = (x=300, y=200)
#     name is used for the call-back, and the button text
#
#     :param parent_func: the function to call when the button is clicked.
#     :param filepath: str file-path to the button image
#     :param x: x coordinate
#     :param y: y coordinate
#     :return: MenuButton
#     """
#     window_size = pygame.display.get_window_size()
#     xa = window_size[0] / 3
#     ya = window_size[1] / 3
#     if x:
#         x_butt = xa * x
#     else:
#         x_butt = xa
#     if y:
#         y_butt = ya * y
#     else:
#         y_butt = ya
#
#     return MenuButton(filepath=filepath, placement=(x_butt - (75 / 2), y_butt), parent_func=parent_func)

#
# class MainMenu(BaseState):
#
#     def __init__(self):
#         super(MainMenu, self).__init__()
#         self.background_image = None
#         self.next = 'level_rand'
#
#         self.start_button = create_button(
#             y=2,
#             parent_func='manager.ButtonHandler.on_click("start_button")'
#         )
#         self.start_button.set_event(bill_event.START_BUTTON)
#
#         self.levels_button = create_button(
#             'images/editor_btn.png',
#             y=2, x=2,
#             parent_func='self.on_click("levels_button")'
#         )
#
#         self.levels_button.set_event(LEVEL_BUTTON)

#     def get_event(self, event):
#         self.start_button.get_event(event)
#         self.levels_button.get_event(event)
#         if event.type == START_BUTTON:
#             self.done = True
#
#     def state_setup(self, player, window):
#         self.background_image = pygame.image.load('images/start_screen.png').convert()
#         window.blit(self.background_image, (0, 0))
#         self.start_button.add(Game.ui_container)
#         self.levels_button.add(Game.ui_container)
#         print("making menu buttons")
#         Game.ui_container.draw(window)
#
#     def on_run(self):
#         pass
#
#     def cleanup(self):
#         print("cleaning menu")
#         Game.ui_container.empty()
#         self.levels_button.remove(Game.ui_container)
#
#         pygame.display.update()
#
#     def render_state(self, window, time_delta):
#         """
#         :type window: pygame.Surface
#         :param window:
#         :param time_delta:
#         :return:
#         """
#         window.blit(self.background_image, (0, 0))
#
#         Game.bg_container.draw(window)
#         Game.ui_container.draw(window)
#
