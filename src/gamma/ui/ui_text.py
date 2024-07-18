import pygame
from ..core.colours import *
from ..renderables.text import Text
from ..core.assets import fontDefaultMedium

pygame.font.init()

# function from:
# https://nerdparadise.com/programming/pygameblitopacity
def blit_alpha(target, source, location, opacity):
    
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

def drawText(s, t, x, y, fg=WHITE, alpha=255, hAlign='left', vAlign='top', underline=False, font=fontDefaultMedium):
    Text(t, x, y, hAlign, vAlign, fg, alpha, font, underline).draw(s)
