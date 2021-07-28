import pygame
from .system import System

class CollisionSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['position', 'collider']
    
    def updateEntity(self, entity, scene):
        
        if scene.world is None:
            return

        # collision with other entities

        for otherEntity in scene.world.entities:
            if entity is not otherEntity:
                if otherEntity.hasComponent('position', 'collider'):
                    
                    # calculate abcolute collider positions
                    
                    # ...for this entity
                    entityPosRect = entity.getComponent('position').rect
                    entityColliderRect = entity.getComponent('collider').rect
                    entityRect = pygame.Rect(
                        entityPosRect.x + entityColliderRect.x,
                        entityPosRect.y + entityColliderRect.y,
                        entityColliderRect.w,
                        entityColliderRect.h
                    )

                    # ...for other entity
                    otherEntityPosRect = otherEntity.getComponent('position').rect
                    otherEntityColliderRect = otherEntity.getComponent('collider').rect
                    otherEntityRect = pygame.Rect(
                        otherEntityPosRect.x + otherEntityColliderRect.x,
                        otherEntityPosRect.y + otherEntityColliderRect.y,
                        otherEntityColliderRect.w,
                        otherEntityColliderRect.h
                    )

                    # respond to a collision if there is one
                    if entityRect.colliderect(otherEntityRect):
                        if entity.getComponent('collider').collisionResponse is not None:
                            entity.getComponent('collider').collisionResponse('entity', otherEntity)

        # collision with world
        if scene.world.map is not None:

            # get the tile at each of the 4 entity collider corners
            # TODO...