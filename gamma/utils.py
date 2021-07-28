import pygame

def drawRect(s,x,y,w,h,c,a=255):
    overlay = pygame.Surface((w,h))
    overlay.set_alpha(a)
    overlay.fill(c)
    s.blit(overlay, (x,y))

def drawBox(s,x,y,w,h,c):
    # top
    pygame.draw.line(s,c,(x,y),(x+w,y))
    # bottom
    pygame.draw.line(s,c,(x,y+h),(x+w,y+h))
    # left
    pygame.draw.line(s,c,(x,y),(x,y+h))
    # right
    pygame.draw.line(s,c,(x+w,y),(x+w,y+h))