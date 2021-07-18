import pygame
import gamma as engine

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

def drawText(s, t, x, y, fg, alpha, align='left', fontTag='munro24'):
    font = engine.resourceManager.getFont(fontTag)
    t = str(t)
    text = font.render(t, True, fg)
    text_rectangle = text.get_rect()

    if align == 'center':
        x -= text_rectangle.width / 2

    text_rectangle.topleft = (x,y)

    blit_alpha(s, text, (x,y), alpha)