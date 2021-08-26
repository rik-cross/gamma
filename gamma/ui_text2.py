from .gamma import resourceManager
from .colours import WHITE
from .renderable import Renderable
import pygame

def blit_alpha(target, source, location, opacity):

    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

class Text(Renderable):

    def __init__(self, text, x, y, colour=WHITE, alpha=255, fontTag='munro24', underline=False, hAlign='left', vAlign='top'):
        
        self.text = str(text)
        self.colour = colour
        self.alpha = alpha
        self.fontTag = fontTag
        self.underline = underline

        self.font = resourceManager.getFont(self.fontTag)
        self.font.set_underline(self.underline)
        self.textSurface = self.font.render(self.text, True, self.colour)
        self.rect = self.textSurface.get_rect()

        self.rect.x = x
        self.rect.y = y

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
        blit_alpha(surface, self.textSurface, (x,y), self.alpha)

