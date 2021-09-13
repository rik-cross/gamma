import pygame
from .system import *
from .gamma import *

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
                for otherEntity in scene.world.entities:

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
                            trigger.current.append(otherEntity)
            
            #
            # execute the relevant trigger function for each collision
            #

            # trigger is 'entered' if only collided this frame
            if trigger.current and not trigger.last:
                trigger.onCollisionEnter(entity)

            # trigger is 'exited' if no longer colliding
            elif not trigger.current and trigger.last:
                trigger.onCollisionExit(entity)
            
            # otherwise it's an ongoing collision
            elif trigger.current:
                trigger.onCollide(entity)