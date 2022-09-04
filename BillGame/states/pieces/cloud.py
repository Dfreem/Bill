import pygame
from pygame import sprite


class Cloud(sprite.Sprite):
    filepath = 'images/desert_back4.png'

    def __init__(self, foreground=False):
        super().__init__()
        self.scroll_speed = 4
        self._is_breakable = False
        self.is_broken = False
        self.win_width, self.win_height = pygame.display.get_window_size()
        self.image = pygame.image.load(Cloud.filepath).convert_alpha()
        if foreground:
            self.in_front()
        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.size

    def in_front(self):
        self.image = pygame.transform.smoothscale(self.image, (800, 550))
        self.image.set_alpha(90)
        self.scroll_speed = 5

    def update(self):
        if self.rect.x > -800:
            self.rect.x -= self.scroll_speed
        else:
            self.rect.x += self.win_width + 800

    @property
    def scroll(self):
        return self.scroll_speed

    @scroll.setter
    def scroll(self, value):
        if 8 >= value >= 0:
            self.scroll_speed = value
