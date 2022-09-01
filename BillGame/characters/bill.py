import pygame
from pygame.sprite import DirtySprite


class BulletBill(DirtySprite):
    bill_vel = 4

    def __init__(self):
        super(BulletBill, self).__init__()
        """
        BulletBill represents the player_container class in this game

        :param kwargs: Optionally provide bills image filepath, x and/or z parameters at time of instantiation
        """
        print("creating bill")
        # ---- numbers ----
        self.x = 100
        self.y = 100
        self.vel_up = 4
        self.vel_down = 4
        self.hp = 100
        self.damage = 20
        self.is_dead = False
        self.boost = 0
        self.filepath: str = "images/bullet_bill.png"
        self.image = pygame.image.load(self.filepath).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.is_hit = self.rect.colliderect(self.rect)

        # ---- image ----

    def take_damage(self, damage):
        """
        Take damage from something in the current state

        :type damage: int
        :param damage: how much damage to take
        :return: None
        """
        if damage and not self.is_dead:
            self.hp -= damage
        if self.hp <= 0:
            self.is_dead = True

    def bang(self):
        print("bang")

    @property
    def x_coord(self):
        return self.x

    @x_coord.setter
    def x_coord(self, value):
        self.x = value

    @property
    def y_coord(self):
        return self.y

    @y_coord.setter
    def y_coord(self, value):
        self.y = value
