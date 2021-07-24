import pygame
from copy import deepcopy
from .component import Component

class Position(Component):

    def __init__(self, x, y, w, h):
        self.key = 'position'
        self.rect = pygame.Rect(x, y, w, h)
        self.initialRect = pygame.Rect(x, y, w, h)

    def reset(self):
        self.rect = deepcopy(self.initialRect)

    def touching(self, otherEntity):
        if not otherEntity.hasComponent('position'):
            return False
        return self.rect.colliderect(otherEntity.getComponent('position').rect)