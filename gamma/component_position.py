import pygame
from copy import deepcopy
from .component import Component

class PositionComponent(Component):

    def __init__(self, x, y, w, h, xAnchor='left', yAnchor='top', angle=90, rotationStyle='none'):

        self.key = 'position'
        self.rect = pygame.Rect(x, y, w, h)
        self.initialRect = pygame.Rect(x, y, w, h)

        # store position anchor points
        self.xAnchor = xAnchor
        self.yAnchor = yAnchor
        self.calculatePositionUsingAnchors()

        self.angle = angle
        self.rotationStyle = rotationStyle

    def calculatePositionUsingAnchors(self):

        # adjust x position for horizontal anchor
        if self.xAnchor == 'center':
            self.rect.x -= (self.rect.w/2)
        if self.xAnchor == 'right':
            self.rect.x -= (self.rect.w)
        
        # adjust y position for vertical anchor
        if self.yAnchor == 'middle':
            self.rect.y -= (self.rect.h/2)
        if self.yAnchor == 'bottom':
            self.rect.y -= (self.rect.h)

    def reset(self):
        self.rect = deepcopy(self.initialRect)

    def setSize...

    def touching(self, otherEntity):
        if not otherEntity.hasComponent('position'):
            return False
        return self.rect.colliderect(otherEntity.getComponent('position').rect)
    
    # getters and setters for position

    # x

    @property
    def x(self):
        return self.rect.x
    
    @x.setter
    def x(self, value):
        self.rect.x = value

    # y

    @property
    def y(self):
        return self.rect.y
    
    @y.setter
    def y(self, value):
        self.rect.y = value
    
    # w

    @property
    def w(self):
        return self.rect.w
    
    @w.setter
    def w(self, value):
        self.rect.w = value

    # h

    @property
    def h(self):
        return self.rect.h
    
    @h.setter
    def h(self, value):
        self.rect.h = value    

    # getters and setters for anchor points

    # center

    @property
    def center(self):
        return self.rect.x + (self.rect.w/2)

    @center.setter
    def center(self, value):
        self.xAnchor = 'center'
        self.rect.x = value - (self.rect.w / 2)

    # right

    @property
    def right(self):
        return self.rect.x + self.rect.w

    @right.setter
    def right(self, value):
        self.xAnchor = 'right'
        self.rect.x = value - self.rect.w

    # middle

    @property
    def middle(self):
        return self.rect.y + (self.rect.h/2)

    @middle.setter
    def middle(self, value):
        self.yAnchor = 'middle'
        self.rect.y = value - (self.rect.h / 2)

    # bottom

    @property
    def bottom(self):
        return self.rect.y + self.rect.h

    @bottom.setter
    def bottom(self, value):
        self.yAnchor = 'middle'
        self.rect.y = value - self.rect.h