import pygame
import game
from states.menu import MainMenu
from states.random_level import LevelRand

"""
Algorythm
This is the entry point:
 - first initializing some settings, variables to pass in to the game instance.
 - create instance of game, passing in settings.
 - after instantiating the game object, then we can assemble the state dictionary.
 - the game object is passed off to a new instance of state manager.
 - state manager helps instantiate and switches states. 
  This keeps the game class from needing to import any instances.
"""

# TODO level editor mechanics

if __name__ == '__main__':

    '''These settings may be changed depending on the display you are on or your desired window size.
    while the game is not optimized for other sizes yet, it is runnable at other sizes.
    if changing the fps or size, it should be done here.'''
    SETTINGS = {
        'win_width': 1200,
        'win_height': 600,
        'fps': 60,
        'sky_color': pygame.Color('#B4D0F0')
    }

    print("instantiating game\n...\n...")

    # instantiate _game first then make the game-states, in this order.
    _game = game.Game(**SETTINGS)

    '''new levels are added to the game here'''
    states = {
        "main_menu": MainMenu(),
        "level_rand": LevelRand(),
    }
    # beginning state is main menu
    _game.setup_states("main_menu", **states)

    # once the game settings are implemented we begin the game loop.
    # the game loop can be found in game.py
    _game.main_loop()
    print("game created, manager created, :init")


