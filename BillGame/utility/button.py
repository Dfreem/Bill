import pygame
from pygame.sprite import Sprite, AbstractGroup


class MenuButton(Sprite):

    def __init__(self, filepath=None, placement=(0, 0), parent_func='print("not implemented")'):
        """
        game button model.

        :param text: the text on the button and the name sent as on_click.
        :param size: button size
        :param placement: where to put the button on the game window
        :param parent_func: a string representation of the method inside the parent state,
        to call when this button is clicked.
        """
        super(MenuButton, self).__init__()

        self.butt_event = None
        # default filepath if none is given
        if filepath is None:
            filepath = "images/start_btn.png"
        self.image = pygame.image.load(filepath)

        # temporary rect holder, don't delete
        self.rect = self.image.get_rect()
        self.is_clicked = False
        # can't beat 'em, join em.
        self.update = super().update
        size = self.rect.size

        # default location of button if None is given
        if placement == (0, 0):
            placement = (400 - size[0], 250 - size[1])

        # real rect, used for placement on-screen
        self.rect = pygame.rect.Rect(placement, size)

        # parent function should be a callable method inside the same state as this button.
        # self.parent_func = parent_func
        """
        a string (repr)esentaion of the method in the parent class (not the super) 
        that this button will call when it is clicked.
        
         this should be callable with :method:`exec(parent_func)`
        """

    def get_event(self, event):
        """
        the MenuButton class uses get_event to monitor for mouse clicks.

        :param event: events from the main gain loop in the Game class.
        :return:  None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_butt = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_butt[0]:
                if self.rect.x <= mouse_x <= self.rect.x + self.rect.width:
                    if self.rect.y <= mouse_y <= self.rect.y + self.rect.height:
                        print(mouse_x, mouse_y, mouse_butt, "click")
                        pygame.event.post(pygame.event.Event(self.butt_event))

    def add(self, *groups: AbstractGroup) -> None:
        """
        MenuButton overrides the add method from its super-class, Sprite,
        in order to make management and transfer easier.
        The only thing that takes place is mapping this to the same method in the super.

        :param groups: The group/s this button is to be added to.
        :return: None
        """
        super(MenuButton, self).add(*groups)

    def set_event(self, new_event):
        self.butt_event = new_event

    @property
    def click(self):
        return self.is_clicked

    @click.setter
    def click(self, value):
        self.is_click = value
