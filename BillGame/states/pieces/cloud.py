import pygame

from states.pieces import brick


class Cloud(brick.Brick):
    filepath = "images/desert_back4.png"

    def __init__(self, foreground=False):
        super().__init__()
        self.image = pygame.image.load(Cloud.filepath).convert_alpha()
        if foreground:
            self.in_front()
        self.rect = self.image.get_rect()

    def in_front(self):
        self.image = pygame.transform.smoothscale(self.image, (800, 550))
        self.image.set_alpha(90)
