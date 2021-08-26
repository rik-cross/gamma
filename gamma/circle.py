from .colours import WHITE
from .renderable import Renderable
#from .ui_text import blit_alpha
import pygame

def blit_alpha(target, source, location, opacity):

    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

class Circle(Renderable):

    def __init__(self, x, y, r, colour=WHITE, alpha=255):
        
        self.colour = colour
        self.alpha = alpha

        self.x = x
        self.y = y
        self.r = r

    def draw(self, surface, xOff=0, yOff=0, scale=1):
        x = int(self.x * scale + xOff)
        y = int(self.y * scale + yOff)
        r = int(self.r * scale)
        pygame.draw.circle(surface, self.colour, (x, y), r)


