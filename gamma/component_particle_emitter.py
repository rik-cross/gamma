import pygame
from .particle import *
from .colours import *
import random

class ParticleEmitterComponent:
    
    def __init__(self, size=20,
        colour=LIGHT_GREY,
        xOff=0,
        yOff=0,
        lifetime=60,
        emit_frequency=10
        ):
        
        self.key = 'emitter'
        
        self.particles = []
        self.timer = 0
        self.lifetime = lifetime
        self.destroy = False
        self.finished = False
        self.size = size
        self.colour = colour
        self.xOff = xOff
        self.yOff = yOff
        self.emit_frequency = emit_frequency
    
    def update(self, parentPosX, parentPosY):
 
        # delete particles
        for p in self.particles:
            if p.destroy:
                self.particles.remove(p)
        
        # timer to add particles
        self.timer -= 1
        if self.timer <= 0 and self.finished is False:
            self.timer = self.emit_frequency
            x = round(random.uniform(-2,2), 3)
            y = round(random.uniform(-2,2), 3)
            self.particles.append(Particle(pygame.math.Vector2(parentPosX+self.xOff,parentPosY+self.yOff), pygame.math.Vector2(x,y), self.size, self.colour))
        
        # update all particles
        for p in self.particles:
            p.update()
        
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.lifetime = 0
            self.finished = True
    
        if self.finished is True:
            if len(self.particles) == 0:
                self.destroy = True

    def draw(self, scene):

        # draw all particles
        for p in self.particles:
            p.draw(scene)