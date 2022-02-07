import pygame
from .system import *
from .rectangle import Rectangle
from .colours import *

class Battleystem(System):

    def init(self):
        self.key = 'battle'

    def setRequirements(self):
        self.requiredComponents = ['battle', 'position']

    def updateEntity(self, entity, scene):
        
        btl = entity.getComponent('battle')
        pos = entity.getComponent('position')

        currentHitbox = btl.getHitbox(entity.state)

        if currentHitbox is None:
            return

        entityHitRect = pygame.Rect(
            pos.x + currentHitbox.x,
            pos.y + currentHitbox.y,
            currentHitbox.w,
            currentHitbox.h
        )
        
        otherEntities = scene.getEntitiesWithComponent('battle', 'position')
        otherEntities.remove(entity)

        if entity.prevState != entity.state:
            for h in btl.hitboxes:
                btl.hitboxes[h].entityHitList = []

        for e in otherEntities:

            o_btl = e.getComponent('battle')
            o_pos = e.getComponent('position')

            o_currentHurtbox = o_btl.getHurtbox(e.state)

            if o_currentHurtbox is None:
                continue

            otherEntityHurtRect = pygame.Rect(
                o_pos.x + o_currentHurtbox.x,
                o_pos.y + o_currentHurtbox.y,
                o_currentHurtbox.w,
                o_currentHurtbox.h
            )

            if entityHitRect.colliderect(otherEntityHurtRect):
                if o_currentHurtbox.hurtOnce is False or e not in currentHitbox.entityHitList:
                    currentHitbox.hitFunction(entity, e)
                    if o_currentHurtbox.hurtOnce and e not in currentHitbox.entityHitList:
                        currentHitbox.entityHitList.append(e)

    def drawEntity(self, entity, scene):

        return

        btl = entity.getComponent('battle')
        pos = entity.getComponent('position')

        # draw hitbox in green
        if entity.state in btl.hitboxes.keys():
            hitbox = btl.hitboxes[entity.state]
            scene.renderer.add(Rectangle(
                pos.x + hitbox.x,
                pos.y + hitbox.y,
                hitbox.w, hitbox.h,
                colour=GREEN), scene=False
            )

        # draw hurtbox in red
        if entity.state in btl.hurtboxes.keys():
            hurtbox = btl.hurtboxes[entity.state]
            scene.renderer.add(Rectangle(
                pos.x + hurtbox.x,
                pos.y + hurtbox.y,
                hurtbox.w, hurtbox.h,
                colour=RED), scene=False
            )