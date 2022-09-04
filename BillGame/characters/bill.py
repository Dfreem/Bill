import pygame
from pygame.sprite import DirtySprite, Sprite


class BulletBill(Sprite):
    bill_vel = 3

    def __init__(self):
        super(BulletBill, self).__init__()
        """
        BulletBill represents the player_container class in this game

        :param kwargs: Optionally provide bills image filepath, x and/or z parameters at time of instantiation
        """
        print("creating bill")
        # ---- numbers ----
        self.vel_up = self.bill_vel
        self.vel_down = self.bill_vel
        self.hp = 100
        self.damage = 20
        self.is_dead = False
        self._boost = 0
        self.top_speed = 8
        self.filepath: str = "images/bullet_bill.png"
        self.image = pygame.image.load(self.filepath).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = pygame.rect.Rect((200, 100), (100, 100))
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
            print("dead")
            self.is_dead = True

    @property
    def x_coord(self):
        return self.rect.x

    @x_coord.setter
    def x_coord(self, value):
        self.rect.x = value

    @property
    def y_coord(self):
        return self.rect.y

    @y_coord.setter
    def y_coord(self, value):
        self.rect.y = value

    def get_event(self, event):
        pass

    @property
    def boosted(self):
        return self._boost

    @boosted.setter
    def boosted(self, value):
        self._boost = value
