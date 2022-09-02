import pygame

from BillGame.utility.button import MenuButton


def update_fps(fps):

    font = pygame.font.SysFont("Futura", 18)
    fps_text = font.render(f'fps: {fps}', False, 'black')
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

