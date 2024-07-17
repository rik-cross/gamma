import pygame
import os
from math import floor
from ..core.system import System
from ..core.colours import *
from ..renderables.image import Image

class EmoteSystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_emote import EmoteComponent
        from ..components.component_position import PositionComponent
        self.requiredComponents = [EmoteComponent, PositionComponent]
    
    def updateEntity(self, entity, scene):
        from ..components.component_emote import EmoteComponent
        from ..components.component_tags import TagsComponent
        #update
        em = entity.getComponent(EmoteComponent)
        em.update()

        # destroy if required
        if em.destroy:
            entity.removeComponent(EmoteComponent)
        
        # delete the entity if it serves only as a particle emitter
        if entity.getComponent(TagsComponent).has('emote'):
            scene.deleteEntity(entity)
    
    def drawEntity(self, entity, scene):
        
        from ..components.component_emote import EmoteComponent
        from ..components.component_position import PositionComponent

        emoteComponent = entity.getComponent(EmoteComponent)
        positionComponent = entity.getComponent(PositionComponent)

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
        #scene.renderer.add(Image(
        #    pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + '/../images/heart.png'),
        #    positionComponent.x + positionComponent.w//2,
        #    positionComponent.y - imageRect.h//2 - emoteComponent.bottomMargin,
        #    w=32, h=32,
        #    hAlign='center',
        #    vAlign='middle'
        #), scene=False)

        # image
        scene.renderer.add(Image(
            image,
            positionComponent.x + positionComponent.w//2,
            positionComponent.y - imageRect.h//2 - emoteComponent.bottomMargin - 3,
            w=w, h=h,
            hAlign='center',
            vAlign='middle'
        ), scene=False)

