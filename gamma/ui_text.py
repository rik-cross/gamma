import pygame
from .colours import *
from .ui_text2 import Text

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

def drawText(s, t, x, y, fg=WHITE, alpha=255, hAlign='left', vAlign='top', underline=False, fontTag='munro24'):
    Text(t, x, y, fg, alpha, fontTag, underline, hAlign, vAlign).draw(s)
