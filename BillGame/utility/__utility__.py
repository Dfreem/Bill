import random

import pygame

from utility.button import MenuButton


def update_fps(fps, hp):

    font = pygame.font.SysFont("Futura", 18)
    fps_text = font.render(f'fps: {int(fps)}\nplayer hp: {hp}', False, 'lightgreen')
    surf = pygame.Surface((30, 20)).convert_alpha()
    surf.fill("blanchedalmond")
    return fps_text


def create_button(filepath=None, x=None, y=None):
    """
    Create specialized buttons for the main menu, but will work for other buttons.
    x and y are optional. the screen is divided into thirds. Giving x or y or both,
    moves the placement of the button by 1 third of the screen size in the given direction.
    this means that giving 3 puts the button at the very edge of the screen, and anything mor than 3 places it
    outside if the visible window.

    :type filepath: str
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

    return MenuButton(filepath=filepath, placement=(x_butt - (75 / 2), y_butt))


def rand_spot(thing, window):
    """
    :type thing: object { object.x, object.y }
    :param thing: the thing to move. The object must have and self.x and self.y
    :type window: pygame.Surface
    :param window: the game window
    """
    x, y = window.get_size()
    thing.rect.x = random.randint(-600, x + 600)
    thing.rect.y = random.randint(0, y)
    return thing


class BrickHead:
    def __init__(self):
        self.next_item= None
        self.x = 0
        self.y = 0
        self.direction = 1
        self._speed = 4
        self.hopper = []
        self.hopper_is_empty = True
        self.rect = pygame.rect.Rect((self.x, self.y), (0, 0))

    def fill_hopper(self, *items):
        self.hopper.append(*items)
        self.hopper_is_empty = False

    def in_motion(self, window):
        """
        :type window: pygame.Surface
        """
        limit_y = window.get_size()[0]

        if not self.hopper_is_empty:

            if self.y <= limit_y + 100 and self.direction == 1:
                self.y += self._speed
                if not self.y <= limit_y + 100:
                    self.direction = 0
            elif self.y >= 0 and self.direction == 0:
                self.y -= self._speed
                if not self.y >= 0:
                    self.direction = 1

    def drop(self, window):
        if not self.hopper_is_empty:
            window.blit(self.hopper[0], (self.x, self.y))
            # much the front spite to the back of the line
            self.hopper.append(self.hopper.pop(0))

    def update(self, delta_time):
        # TODO stopped here,
        #  this needs to compare to delta time and release on self.frequency
        pass

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if 1 <= value <= 10 and value == type(int):
            self.speed = value

