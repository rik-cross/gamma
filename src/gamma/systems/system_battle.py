import pygame
from ..core.system import *
from ..core.colours import *
from ..renderables.rectangle import Rectangle

class Battleystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_battle import BattleComponent
        from ..components.component_position import PositionComponent
        self.requiredComponents = [BattleComponent, PositionComponent]

    def updateEntity(self, entity, scene):
        from ..components.component_battle import BattleComponent
        from ..components.component_position import PositionComponent
        btl = entity.getComponent(BattleComponent)
        pos = entity.getComponent(PositionComponent)

        currentHitbox = btl.getHitbox(entity.state)

        if currentHitbox is None:
            return

        entityHitRect = pygame.Rect(
            pos.x + currentHitbox.x,
            pos.y + currentHitbox.y,
            currentHitbox.w,
            currentHitbox.h
        )
        
        otherEntities = scene.getEntitiesWithComponent(BattleComponent, PositionComponent)
        otherEntities.remove(entity)

        if entity.prevState != entity.state:
            for h in btl.hitboxes:
                btl.hitboxes[h].entityHitList = []

        for e in otherEntities:

            o_btl = e.getComponent(BattleComponent)
            o_pos = e.getComponent(PositionComponent)

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

        from ..components.component_battle import BattleComponent
        from ..components.component_position import PositionComponent

        btl = entity.getComponent(BattleComponent)
        pos = entity.getComponent(PositionComponent)

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