# This was taken from www.scriptefun.com/transcript-2-using
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame


class SpriteSheet(object):
    """
    SpriteSheet class handles the loading and processing of sprite-sheets.

     ::

    non-sprite_sheet based images can also make use of this class as well,
    by only using the init method and none of the others contained in this class.

    ---------------
    """
    def __init__(self, filename):

        try:
            self.image = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Unable to load sprite-image image:', filename)
            raise SystemExit(message)
    # Load a specific image from a specific rectangle

    def image_at(self, rectangle, color_key=None):
        """Loads image from x,y,x+offset,y+offset"""

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.image, (0, 0), rect)

        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        return image

    def images_at(self, rects, color_key=None):
        """Loads multiple images, supply a list of coordinates"""

        return [self.image_at(rect, color_key) for rect in rects]
    # Load a whole strip of images

    def load_strip(self, rect, image_count, color_key=None):
        """
        Load a strip of images and return them as a list

        This method is used in use with sprite sheets,
        in which it is common to have one character's animation,
        in the form of one strip of images.
        :type rect: pygame.Rect
        :param rect: A pygame.Rect with dimensions relating to the size
         and location of the first frame on the image.
         :type image_count: int
        :param image_count: how many images are contained on the strip.
        :type color_key:
        :param color_key:
        :return:
        """
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, color_key)
