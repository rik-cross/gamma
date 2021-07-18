import pygame
from .system import *
from .colours import *
import random

class PhysicsSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['position', 'collider']
    
    def updateEntity(self, entity, scene):

        #
        # use the entity intentions to update the transform component
        #

        # vertical transform

        if entity.hasComponent('intention'):
            entityIntention = entity.getComponent('intention')
            if entityIntention.jump and entity.on_ground:
                engine.soundManager.playSound('jump')
                entity.state = 'jumping'
                if entity.hasComponent('motion'):
                    entity.getComponent('motion').velocity.y = -7

        if entity.hasComponent('motion'):
            motionComponent = entity.getComponent('motion')
            motionComponent.velocity.y += motionComponent.acceleration.y
            entity.getComponent('transform').position.y = entity.getComponent('position').rect.y + motionComponent.velocity.y

        # horizontal transform

        entity.getComponent('transform').position.x = entity.getComponent('position').rect.x + entity.getComponent('motion').velocity.x

        #if entity.intention is not None:
        if entity.hasComponent('intention'):
            intentionComponent = entity.getComponent('intention')
            if intentionComponent.moveLeft:
                #entity.transform.position.x -= 3
                entity.getComponent('transform').position.x -= 3
                entity.direction = 'left'
                entity.state = 'walking'
            if intentionComponent.moveRight:
                #entity.transform.position.x += 3
                entity.getComponent('transform').position.x += 3
                entity.direction = 'right'
                entity.state = 'walking'
            if not intentionComponent.moveLeft and not intentionComponent.moveRight:
                entity.state = 'idle'

        #
        # use the transform component to check for and resolve collisions
        #

        # vertical collisions

        positionComponent = entity.getComponent('position')
        colliderComponent = entity.getComponent('collider')
        transformComponent = entity.getComponent('transform')

        new_y_rect = pygame.Rect(
            int(positionComponent.rect.x + colliderComponent.rect.x),
            int(transformComponent.position.y + colliderComponent.rect.y),
            colliderComponent.rect.width,
            colliderComponent.rect.height)
        
        y_collision = False
        entity.on_ground = False

        #...check against tile map
        
        topLeftTile = engine.world.map.getTileAtPosition(new_y_rect.x, new_y_rect.y)
        topRightTile = engine.world.map.getTileAtPosition(new_y_rect.x + new_y_rect.w, new_y_rect.y)
        bottomLeftTile = engine.world.map.getTileAtPosition(new_y_rect.x, new_y_rect.y + new_y_rect.h)
        bottomRightTile = engine.world.map.getTileAtPosition(new_y_rect.x + new_y_rect.w, new_y_rect.y + new_y_rect.h)

        positionComponent = entity.getComponent('position')
        transformComponent = entity.getComponent('transform')
        motionComponent = entity.getComponent('motion')

        if topLeftTile.solid or topRightTile.solid or bottomLeftTile.solid or bottomRightTile.solid:

            y_collision = True
            if abs(motionComponent.velocity.y) > 10:
                entity.trauma += 0.7 # TODO -- set max
                if entity.getComponent('tags').has('player'):
                    engine.world.entities.append(engine.entityFactory.create('collision', positionComponent.rect.x+(positionComponent.rect.w/2), positionComponent.rect.y + colliderComponent.rect.h))
                    engine.soundManager.playSound('explosion_small', engine.soundManager.soundVolume / 2)
            motionComponent.velocity.y = 0

            if bottomLeftTile.solid or bottomRightTile.solid:
                positionComponent.rect.y = ((int((transformComponent.position.y + colliderComponent.rect.y + colliderComponent.rect.h) // engine.world.map.tileSize))*engine.world.map.tileSize) - positionComponent.rect.height + 2 # TODO -- include collider??
                entity.on_ground = True

        if y_collision == False:
            positionComponent.rect.y = int(transformComponent.position.y)

        # horizontal collisions
        
        new_x_rect = pygame.Rect(
            int(transformComponent.position.x + colliderComponent.rect.x),
            int(positionComponent.rect.y + colliderComponent.rect.y-1),
            colliderComponent.rect.width,
            colliderComponent.rect.height)
        
        x_collision = False

        topLeftTile = engine.world.map.getTileAtPosition(new_x_rect.x, new_x_rect.y)
        topRightTile = engine.world.map.getTileAtPosition(new_x_rect.x + new_x_rect.w, new_x_rect.y)
        bottomLeftTile = engine.world.map.getTileAtPosition(new_x_rect.x, new_x_rect.y + new_x_rect.h - 2)
        bottomRightTile = engine.world.map.getTileAtPosition(new_x_rect.x + new_x_rect.w, new_x_rect.y + new_x_rect.h - 2)

        # check in the middle of the player too?
        # need a better way that this -- for larger entities
        middleLeftTile = engine.world.map.getTileAtPosition(new_x_rect.x, new_x_rect.y + (new_x_rect.h / 2) - 1)
        middleRightTile = engine.world.map.getTileAtPosition(new_x_rect.x + new_x_rect.w, new_x_rect.y + (new_x_rect.h / 2) - 1)

        positionComponent = entity.getComponent('position')
        transformComponent = entity.getComponent('transform')
        motionComponent = entity.getComponent('motion')

        if topLeftTile.solid or topRightTile.solid or bottomLeftTile.solid or bottomRightTile.solid or middleLeftTile.solid or middleRightTile.solid:

            x_collision = True
            if abs(motionComponent.velocity.x) > 10:
                entity.trauma += 0.7 # TODO -- set max
                if entity.getComponent('tags').has('player'):
                    engine.world.entities.append(engine.entityFactory.create('collision', positionComponent.rect.x+(positionComponent.rect.w/2), positionComponent.rect.y + colliderComponent.rect.h))
                    engine.soundManager.playSound('explosion_small', engine.soundManager.soundVolume / 2)
        if x_collision == False:
            positionComponent.rect.x = transformComponent.position.x

        if entity.getComponent('tags').has('player') and not entity.on_ground:
            entity.state = 'jumping'
        
        # TODO -- replace this with horizontal friction
        if x_collision or y_collision:
            motionComponent.velocity.x = 0

            if entity.getComponent('tags').has('balloon'):
                engine.world.entities.append(engine.entityFactory.create('explosion', positionComponent.rect.x, positionComponent.rect.y))
                engine.soundManager.playSound('explosion_small', engine.soundManager.soundVolume / 2)
                engine.world.entities.remove(entity)