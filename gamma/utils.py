import pygame

def drawRect(s,x,y,w,h,c,a=255):
    overlay = pygame.Surface((w,h))
    overlay.set_alpha(a)
    overlay.fill(c)
    s.blit(overlay, (x,y))