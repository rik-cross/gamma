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

        em = entity.getComponent('emote')
        em.update()
        if em.destroy:
            entity.removeComponent('emote')
    
    def drawEntity(self, entity, scene):
        
        emoteComponent = entity.getComponent('emote')
        positionComponent = entity.getComponent('position')

        image = emoteComponent.image
        imageRect = image.get_rect()
        w = imageRect.w
        h = imageRect.h
        s = 0
        p = 0
        if w >= h:
            s = w
            p = w/20
            w = 20
            h = floor(h / p)
        else:
            s = h
            p = h/20
            h = 20
            w = floor(w / p)

        # box
        scene.renderer.add(Image(
            pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/images/emote_box.png'),
            positionComponent.x + positionComponent.w//2,
            positionComponent.y - imageRect.h//2 - emoteComponent.bottomMargin,
            w=32, h=32,
            hAlign='center',
            vAlign='middle'
        ))

        # image
        scene.renderer.add(Image(
            image,
            positionComponent.x + positionComponent.w//2,
            positionComponent.y - imageRect.h//2 - emoteComponent.bottomMargin - 2,
            w=w, h=h,
            hAlign='center',
            vAlign='middle'
        ))

