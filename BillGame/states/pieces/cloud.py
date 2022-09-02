import pygame

from BillGame.states.pieces import brick


class Cloud:
    filepath = 'images/desert_back4.png'

    def __init__(self, foreground=False):
        super().__init__()
        self.image = pygame.image.load(Cloud.filepath).convert_alpha()
        if foreground:
            self.in_front()
        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.size

    def in_front(self):
        self.image = pygame.transform.smoothscale(self.image, (800, 550))
        self.image.set_alpha(90)
