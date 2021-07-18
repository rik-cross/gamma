from .particle import *
from .colours import *
import random

class ParticleEmitter:
    
    def __init__(self, size=20, colour=LIGHT_GREY):
        self.key = 'emitter'
        self.particles = []
        self.timer = 0
        self.lifetime = 30
        self.destroy = False
        self.finished = False
        self.size = size
        self.colour = colour
    
    def update(self, parentPosX, parentPosY):
 
        # delete particles
        for p in self.particles:
            if p.destroy:
                self.particles.remove(p)
        
        # ues timer to add particles
        self.timer -= 1
        if self.timer <= 0 and self.finished is False:
            self.timer = 10
            x = round(random.uniform(-2,2), 3)
            y = round(random.uniform(-2,2), 3)
            self.particles.append(Particle(pygame.math.Vector2(parentPosX,parentPosY), pygame.math.Vector2(x,y), self.size, self.colour))
        
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

    def draw(self, screen):

        # draw all particles
        for p in self.particles:
            p.draw(screen)