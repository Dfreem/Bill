from abc import abstractmethod, ABC


class BaseState(ABC):
    """
     **b.b.b.b.b.b¡¡¡BassState!!!®** for this game. Levels, States or Menus
    need to inherit this class in order to be played.

    --------------

     States that inherit from this should include the following

     properties:
      + :property:`is_paused`: :class:`bool`
      + :property:`done`: :class:`bool`
      + :property:`quit`: :class:`bool`
      + :property:`next`: :class:`str`
      + :property:`previous`: :class:`str`

    methods:
     - :method:`state_setup(self, player, window, manager)`
     - :method:`on_run(self)`
     - :method:`get_event(self,` :class:`pygame.event.Event`)
     - :method:`cleanup(self,` :class:`pygame.event.Event`)
     - :method:`pause(self)`
       - **inherited**
     - :method:`update(self, delta_time)`
     - :method:`button_clicked(self, button)`

    """

    def __init__(self):
        self._done = False
        self._quit = False
        self._next = None
        self._previous = None

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, value):
        if self.done is not value:
            self._done = value

    @abstractmethod
    def state_setup(self, player, window):
        """
        called when game state is ready to switch to this state.
        Player and window possession transfer should happen here.

        :param player: the character controlled by the players inputs.
        :type window: pygame.Surface
        :param window: The game window.
        :return: None
        """

    @abstractmethod
    def on_run(self):
        """
        called to start the game loop in the context of this state.

        :return: None
        """
        pass

    @abstractmethod
    def get_event(self, event):
        """
        Pass a single event in to the state.

        :type event: pygame.event.Event
        :param event: the event to process.
        :return: None
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        Called when about to switch away from this states' context.

        :return: None
        """
        print("cleaning up...")

    @abstractmethod
    def render_state(self, window, time_delta):
        """
        Called once per frame, should be used to call any drawing method.

        """
        pass
