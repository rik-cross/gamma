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

class Rectangle(Renderable):

    def __init__(self, x, y, w, h, colour=WHITE, alpha=255, hAlign='left', vAlign='top'):
        
        self.colour = colour
        self.alpha = alpha

        self.rect = pygame.Rect(x, y, w, h)

        # adjust x position for horizontal anchor
        if hAlign == 'center':
            self.rect.centerx = self.rect.x
        if hAlign == 'right':
            self.rect.right = self.rect.x

        # adjust y position for vertical anchor
        if vAlign == 'middle':
            self.rect.centery = self.rect.y
        if vAlign == 'bottom':
            self.rect.bottom = self.rect.y

    def draw(self, surface, xOff=0, yOff=0, scale=1):
        x = self.rect.x * scale + xOff
        y = self.rect.y * scale + yOff
        w = self.rect.w * scale
        h = self.rect.h * scale
        adjustedRect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(surface, self.colour, adjustedRect)

