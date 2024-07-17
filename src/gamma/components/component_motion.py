import pygame
import copy

from ..core.component import Component

class MotionComponent(Component):

    def __init__(self, velocity=None, acceleration=None):
        if velocity is None:
            self.velocity = pygame.math.Vector2()
        else:
            self.velocity = velocity
        self.initialVelocity = copy.deepcopy(self.velocity)
        
        if acceleration is None:
            self.acceleration = pygame.math.Vector2()
        else:
            self.acceleration = acceleration
        self.initialAcceleration = copy.deepcopy(self.acceleration)
    
    def reset(self):
        self.velocity = copy.deepcopy(self.initialVelocity)
        self.acceleration = copy.deepcopy(self.initialAcceleration)