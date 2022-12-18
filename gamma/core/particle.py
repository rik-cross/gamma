from math import ceil
from .colours import *
from ..renderables.circle import Circle
from ..renderables.rectangle import Rectangle

class Particle:
    
    def __init__(self,
    
        # required parameters
        position,
        velocity,
        size,

        # optional parameters
        colour = LIGHT_GREY,
        decay = 0.5,
        alphaDecay = 2,
        startingAlpha = 255,
        # shape can be either circle or square
        shape = 'circle',
        lifetime = 1000
    
    ):

        # store required data
        self.pos = position
        self.velocity = velocity
        self.size = size

        # store optional data
        self.colour = colour
        self.decay = decay
        self.alpha = startingAlpha
        self.alphaDecay = alphaDecay
        self.shape = shape
        self.lifetime = lifetime

        # other particle data
        self.destroy = False
    
    def update(self):

        # update particle lifetime
        self.lifetime -= 1
        # destroy if lifetime is over
        if self.lifetime <= 0:
            self.destroy = True

        # update size
        self.size -= self.decay
        # destroy if the particle disappears
        if self.size <= 0:
            self.destroy = True
    
        # update position
        self.pos += self.velocity

        # update alpha
        self.alpha -= self.alphaDecay
        if self.alpha <= 0:
            self.destroy = True
    
    def draw(self, scene):

        if self.shape == 'circle':
            
            scene.renderer.add(Circle(
                self.pos.x, self.pos.y, ceil(self.size/2),
                hAlign='center', vAlign='middle',
                colour=self.colour,
                alpha=self.alpha
            ), scene=False)
        
        else:

            scene.renderer.add(Rectangle(
                self.pos.x, self.pos.y, self.size, self.size,
                hAlign='center', vAlign='middle',
                colour=self.colour,
                alpha=self.alpha
            ), scene=False)
