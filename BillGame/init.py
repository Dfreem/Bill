import pygame
import game
from utility import manager

"""
Meta - scope algorythm
This file starts the motion of the game,
 - first initializing some settings, variables to pass in to the game instance.
 - create instance of game, passing in settings.
 - after instantiating the game object, then we can assemble the state dictionary.
 - the game object is passed off to a new instance of state manager.
 - state manager helps instantiate and switches states. 
  This keeps the game class from needing to import any instances.
"""

# TODO level editor mechanics

if __name__ == '__main__':

    SETTINGS = {
        'win_width':1000,
        'win_height': 800,
        'fps': 60,
        'sky': pygame.Color('#B4D0F0')
    }

    print("instantiating game\n...\n...")

    # instantiate _game first then make the contexts
    _game = game.Game(**SETTINGS)
    _manager = manager.StateManager(_game)
    print("game created, manager created, :init")


