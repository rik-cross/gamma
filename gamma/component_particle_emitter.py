import pygame
from .particle import *
from .colours import *
import random

class ParticleEmitterComponent:
    
    def __init__(self,
    
        #
        # emitter parameters
        #

        # particles spawn in a random position
        # within the emitter's 

        # offset
        xOff = 0, yOff = 0,
        # size
        width = 1, height = 1,
        
        # frame delay between emitting particles
        emit_delay = 2,
        # how many frames the emitter lasts for
        # (set to -1 to never destroy)
        lifetime = 60,
        
        #
        # particle parameters
        #

        # starting size
        particle_size = 30,
        particle_colour = LIGHT_GREY,
        # reduction in particle size per frame
        particle_size_decay = 0.5,
        # reduction in particle alpha per frame
        particle_alpha_decay = 3,
        # how long the particles last
        # (not required if size/alpha decay > 0)
        particle_lifetime = 1000,
        # particle shape is 'circle' or 'square'
        particle_shape = 'circle',

        # particle velocities
        minXVel = -2,
        maxXVel = 2,
        minYVel = -2,
        maxYVel = 2,
    
    ):
        
        self.key = 'emitter'
        
        self.particles = []

        # initialise emitter parameters
        self.xOff = xOff
        self.yOff = yOff
        self.width = width
        self.height = height
        self.emit_delay = emit_delay
        self.lifetime = lifetime
        
        # initialise particle parameters
        self.particle_size = particle_size
        self.colour = particle_colour
        self.particle_size_decay = particle_size_decay
        self.particle_alpha_decay = particle_alpha_decay
        self.particle_lifetime = particle_lifetime
        self.particle_shape = particle_shape
        self.minXVel = minXVel
        self.maxXVel = maxXVel
        self.minYVel = minYVel
        self.maxYVel = maxYVel
        
        # initialise other variables
        self.timer = 0
        self.finished = False
        self.destroy = False
    
    def update(self, parentPosX, parentPosY):
 
        # delete particles marked as 'to destroy'
        for p in self.particles:
            if p.destroy:
                self.particles.remove(p)
        
        # timer to create new particles
        if self.timer > -1:
            self.timer -= 1

            # create a new particle if it's time
            if self.timer <= 0 and self.finished is False:
                # reset timer for creating next particle
                self.timer = self.emit_delay
                
                # calculate random position
                px = random.uniform(parentPosX+self.xOff, parentPosX+self.xOff+self.width)
                py = random.uniform(parentPosY+self.yOff, parentPosY+self.yOff+self.height) 
                
                # calculate random velocity
                vx = round(random.uniform(self.minXVel, self.maxXVel), 3)
                vy = round(random.uniform(self.minYVel, self.maxYVel), 3)
                
                # create new particle and add to particles list
                self.particles.append(
                    Particle(
                        # position
                        pygame.math.Vector2(px, py),
                        # velocity
                        pygame.math.Vector2(vx,vy),
                        self.particle_size,
                        decay = self.particle_size_decay,
                        colour = self.colour,
                        lifetime = self.particle_lifetime,
                        shape = self.particle_shape,
                        alphaDecay = self.particle_alpha_decay
                    )
                )
        
        # update all particles
        for p in self.particles:
            p.update()
        
        # emitter is finished if the timer ends
        if self.lifetime > -1:
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.finished = True
    
        # destroy if finished
        if self.finished is True:
            if len(self.particles) == 0:
                self.destroy = True

    def draw(self, scene):
        # draw all particles
        for p in self.particles:
            p.draw(scene)