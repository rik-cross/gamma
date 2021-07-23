import pygame
from .component import Component

# TODO - make position its own class, with .left, .right, .middle, etc. as properties

class TransformComponent(Component):

    def __init__(self, position=pygame.math.Vector2(), rotation=90):
        self.key = 'transform'
        self.position = position
        self.initialPosition = position
        self.rotation = rotation
        self.initialRotation = rotation
    
    def reset(self):
        self.position = self.initialPosition
        self.rotation = self.initialRotation