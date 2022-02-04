import pygame

class Hurtbox:

    def __init__(self, xOff, yOff, w, h, hurtOnce=True):
        self.x = xOff
        self.y = yOff
        self.w = w
        self.h = h
        self.hurtOnce = hurtOnce
    
    def __str__(self):
        return 'Hitbox x=' + str(self.x) + ', y=' + str(self.y) + ', w=' + str(self.w) + ', h=' + str(self.h)
    
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)