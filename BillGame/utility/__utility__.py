import pygame


def update_fps(fps):
    """
    Track frames / second and display on screen.

    this is also currently displaying the count of block and cloud instances

    :param pyclock: the pygame clock used to measure the frames per second.
     must be the same clock that is used to regulate frame rate.
    :return: a surface with the FPS information as text displayed on it.
    """

    font = pygame.font.SysFont("Futura", 18)
    fps_text = font.render(f'fps: {fps}', False, 'black')
    surf = pygame.Surface((30, 20)).convert_alpha()
    surf.fill("blanchedalmond")
    return fps_text
