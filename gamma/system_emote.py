from .system import System
from .image import Image
from .colours import *
import pygame
import os
from math import floor

class EmoteSystem(System):

    def init(self):
        self.key = 'emote'

    def setRequirements(self):
        self.requiredComponents = ['emote', 'position']
    
    def updateEntity(self, entity, scene):
        
        #update
        em = entity.getComponent('emote')
        em.update()

        # destroy if required
        if em.destroy:
            entity.removeComponent('emote')
        
        # delete the entity if it serves only as a particle emitter
        if entity.getComponent('tags').has('emote'):
            scene.world.deleteEntity(entity)
    
    def drawEntity(self, entity, scene):
        
        emoteComponent = entity.getComponent('emote')
        positionComponent = entity.getComponent('position')

        # get image info
        image = emoteComponent.image
        imageRect = image.get_rect()

        # resize the image to be 18x18 max
        w = imageRect.w
        h = imageRect.h
        percentageResize = 0
        # resize based on width if greater
        if w >= h:
            percentageResize = w/18
            w = 18
            h = floor(h / percentageResize)
        # resize based on heightif greater
        else:
            percentageResize = h/18
            h = 18
            w = floor(w / percentageResize)

        # box
        scene.renderer.add(Image(
            pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/images/emote_box.png'),
            positionComponent.x + positionComponent.w//2,
            positionComponent.y - imageRect.h//2 - emoteComponent.bottomMargin,
            w=32, h=32,
            hAlign='center',
            vAlign='middle'
        ), scene=False)

        # image
        scene.renderer.add(Image(
            image,
            positionComponent.x + positionComponent.w//2,
            positionComponent.y - imageRect.h//2 - emoteComponent.bottomMargin - 3,
            w=w, h=h,
            hAlign='center',
            vAlign='middle'
        ), scene=False)

