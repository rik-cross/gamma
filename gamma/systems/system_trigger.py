import pygame
from ..core.system import *

class TriggerSystem(System):

    def init(self):
        self.key = 'trigger'

    def setRequirements(self):
        self.requiredComponents = ['position', 'triggers']

    def updateEntity(self, entity, scene):

        # store components
        trg = entity.getComponent('triggers')
        pos = entity.getComponent('position')

        # check each trigger in the list
        for trigger in trg.triggerList:

            trigger.last = trigger.current
            # trigger list, to allow for multiple trigger collisions
            trigger.current = []

            if trigger.boundingBox is not None:

                # trigger rect for this entity
                adjustedRect = pygame.rect.Rect(
                    pos.rect.x + trigger.boundingBox.x,
                    pos.rect.y + trigger.boundingBox.y,
                    trigger.boundingBox.w,
                    trigger.boundingBox.h
                )

                # check against all other entities
                for otherEntity in scene.entities:

                    if otherEntity.hasComponent('position') and otherEntity.hasComponent('collider'):
                        
                        # get other entity components
                        op = otherEntity.getComponent('position')
                        oc = otherEntity.getComponent('collider')
                        
                        # calculate rect for other entity
                        otherRect = pygame.rect.Rect(
                            op.rect.x + oc.rect.x,
                            op.rect.y + oc.rect.y,
                            oc.rect.w,
                            oc.rect.h
                        )

                        # if entity trigger rect collides with other entity collider
                        if adjustedRect.colliderect(otherRect):
                            # check whether a button press is required:
                            if trigger.checkPress(otherEntity):
                                trigger.current.append(otherEntity)
            
        #
        # execute the relevant trigger function for each collision
        #

        for trigger in trg.triggerList:

            # only process entities in both lists once
            for e in trigger.current + list(set(trigger.last) - set(trigger.current)):

                if e in trigger.current and e not in trigger.last:
                    trigger.onCollisionEnter(entity, e)
                
                elif e not in trigger.current and e in trigger.last:
                    trigger.onCollisionExit(entity, e)
                
                elif e in trigger.current:
                    trigger.onCollide(entity, e)
