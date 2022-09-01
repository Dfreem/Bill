import pygame.display

from game import BaseState, Game
from utility import bill_event
from utility.bill_event import LEVELS_BUTTON, START_BUTTON
from utility.button import MenuButton


def create_button(filepath=None, x=None, y=None, parent_func='print("not implemented in menu")'):
    """
    Create specialized buttons for the main menu.
    x and y are optional. if both are None, placement = (x=300, y=200)
    name is used for the call-back, and the button text

    :param parent_func: the function to call when the button is clicked.
    :param filepath: str file-path to the button image
    :param x: x coordinate
    :param y: y coordinate
    :return: MenuButton
    """
    window_size = pygame.display.get_window_size()
    xa = window_size[0] / 3
    ya = window_size[1] / 3
    if x:
        x_butt = xa * x
    else:
        x_butt = xa
    if y:
        y_butt = ya * y
    else:
        y_butt = ya

    return MenuButton(filepath=filepath, placement=(x_butt - (75 / 2), y_butt), parent_func=parent_func)


class MainMenu(BaseState):

    def __init__(self):
        super(MainMenu, self).__init__()
        self.background_image = None
        self.next = 'level_rand'
        self.start_button = create_button(y=2, parent_func='manager.ButtonHandler.on_click("start_button")')
        self.start_button.set_event(bill_event.START_BUTTON)
        self.button_handler = pygame.sprite.RenderUpdates()

        self.levels_button = create_button(
            'images/editor_btn.png',
            y=2, x=2,
            parent_func='self.on_click("levels_button")')

        self.levels_button.set_event(LEVELS_BUTTON)

    def get_event(self, event):
        self.start_button.get_event(event)
        self.levels_button.get_event(event)
        if event.type == START_BUTTON:
            self.done = True

    def state_setup(self, player, window):
        self.background_image = pygame.image.load('images/start_screen.png').convert()
        window.blit(self.background_image, (0, 0))
        self.start_button.add(self.button_handler)
        self.levels_button.add(self.button_handler)
        print("making menu buttons")
        self.button_handler.draw(window)

    def on_run(self):
        pass

    def cleanup(self):
        print("cleaning menu")
        self.button_handler.empty()
        self.levels_button.remove(self.button_handler)

        pygame.display.update()

    def render_state(self, window, time_delta):
        """
        :type window: pygame.Surface
        :param window:
        :param time_delta:
        :return:
        """
        window.blit(self.background_image, (0, 0))
        Game.button_handler.draw_ui(window)

