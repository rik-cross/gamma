import pygame
from ..core.system import System

class CollisionSystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_position import PositionComponent
        from ..components.component_collider import ColliderComponent
        self.requiredComponents = [PositionComponent, ColliderComponent]
    
    def updateEntity(self, entity, scene):

        from ..components.component_position import PositionComponent
        from ..components.component_collider import ColliderComponent

        # collisions only happen in a scene
        if scene is None:
            return

        # get components
        pos = entity.getComponent(PositionComponent)
        col = entity.getComponent(ColliderComponent)

        # collision with other entities
        for otherEntity in scene.entities:
            if entity is not otherEntity:

                if otherEntity.hasComponent(PositionComponent, ColliderComponent):
                    
                    # calculate absolute collider positions
                    
                    # ...for this entity
                    entityRect = pygame.Rect(
                        pos.rect.x + col.rect.x,
                        pos.rect.y + col.rect.y,
                        col.rect.w,
                        col.rect.h
                    )

                    # ...for other entity
                    otherEntityPosRect = otherEntity.getComponent(PositionComponent).rect
                    otherEntityColliderRect = otherEntity.getComponent(ColliderComponent).rect
                    otherEntityRect = pygame.Rect(
                        otherEntityPosRect.x + otherEntityColliderRect.x,
                        otherEntityPosRect.y + otherEntityColliderRect.y,
                        otherEntityColliderRect.w,
                        otherEntityColliderRect.h
                    )

                    # respond to a collision if there is one
                    if entityRect.colliderect(otherEntityRect):
                        if col.collisionResponse is not None:

                            # calculate direction(s)
                            directions = []

                            if otherEntityRect.y + otherEntityRect.h > entityRect.y and otherEntityRect.y + otherEntityRect.h < entityRect.y + entityRect.h:
                                directions.append('top')
                            if otherEntityRect.x + otherEntityRect.w > entityRect.x and otherEntityRect.x + otherEntityRect.w < entityRect.x + entityRect.w:
                                directions.append('left')
                            if otherEntityRect.y > entityRect.y:
                                directions.append('bottom')
                            if otherEntityRect.x > entityRect.x:
                                directions.append('right')

                            col.collisionResponse('entity', otherEntity, directions)

        # collision with scene

        if scene.map is not None:
            
            map = scene.map

            # get the tile at each of the 4 entity collider corners
            topLeft     = map.getTileAtPosition(pos.rect.x, pos.rect.y)
            topRight    = map.getTileAtPosition(pos.rect.x + pos.rect.w, pos.rect.y)
            bottomLeft  = map.getTileAtPosition(pos.rect.x, pos.rect.y + pos.rect.h)
            bottomRight = map.getTileAtPosition(pos.rect.x + pos.rect.w, pos.rect.y + pos.rect.h)

            #if topLeft.solid or topRight.solid or bottomLeft.solid or bottomRight.solid:
            if col.collisionResponse is not None:
                collidedTiles = []
                for t in [topLeft, topRight, bottomLeft, bottomRight]:
                    if t is not None:
                        collidedTiles.append(t)
                col.collisionResponse('tile', collidedTiles, [])