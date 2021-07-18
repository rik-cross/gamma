import pygame

class Particle:
    
    def __init__(self, pos, velocity, size, colour):

        self.pos = pos
        self.velocity = velocity
        self.size = size
        self.colour = colour
        self.destroy = False
    
    def update(self):

        # update size
        self.size -= 0.5
        if self.size <= 0:
            self.destroy = True
    
        # update position
        self.pos += self.velocity


