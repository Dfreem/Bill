# TODO pass in current state,
#  create overlay,
#  return state with overlay?
import sys

import pygame


def quit_signal():
    pygame.quit()
    sys.exit()


def pause_box():
    p = pygame.Surface((30, 30))
    p.fill('red')
    return p


def pause(is_paused, window):
    """
    :type is_paused: bool
    :param is_paused: is the game paused?
    :type window: pygame.Surface
    :param window: the game window
    :return: is_paused = False
    """
    while is_paused:
        window.convert_alpha()
        img = pygame.image.load('/Users/devinfreeman/ProgStuff/python/game_rw/images/start_screen.png')
        window.blit(img, (0, 0))
        window.fill(pygame.color.Color(0, 0, 0, 30))
        window.blit(pause_box(), (100, 500))
        pygame.display.update()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.constants.K_p:
            return False

