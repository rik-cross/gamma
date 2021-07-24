import pygame
from copy import deepcopy
from .component import Component

class Position(Component):

    def __init__(self, x, y, w, h, xAnchor='left', yAnchor='top'):

        self.key = 'position'
        self.rect = pygame.Rect(x, y, w, h)
        self.initialRect = pygame.Rect(x, y, w, h)

        # adjust x position for horizontal anchor
        if xAnchor == 'center':
            self.rect.x -= (self.rect.w/2)
        if xAnchor == 'right':
            self.rect.x -= (self.rect.w)
        
        # adjust y position for vertical anchor
        if yAnchor == 'middle':
            self.rect.y -= (self.rect.h/2)
        if yAnchor == 'bottom':
            self.rect.y -= (self.rect.h)

    def reset(self):
        self.rect = deepcopy(self.initialRect)

    def touching(self, otherEntity):
        if not otherEntity.hasComponent('position'):
            return False
        return self.rect.colliderect(otherEntity.getComponent('position').rect)
    
    # setters for anchor points

    # center

    @property
    def center(self):
        return self.rect.x + (self.rect.w/2)

    @center.setter
    def center(self, value):
        self.rect.x = value - (self.rect.w / 2)

    # right

    @property
    def right(self):
        return self.rect.x + self.rect.w

    @right.setter
    def right(self, value):
        self.rect.x = value - self.rect.w

    # middle

    @property
    def middle(self):
        return self.rect.y + (self.rect.h/2)

    @middle.setter
    def middle(self, value):
        self.rect.y = value - (self.rect.h / 2)

    # bottom

    @property
    def bottom(self):
        return self.rect.y + self.rect.h

    @bottom.setter
    def bottom(self, value):
        self.rect.y = value - self.rect.h