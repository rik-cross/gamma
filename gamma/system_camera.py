import pygame
from .system import System
from .colours import *
import random

class CameraSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['camera']
        self.requiresDraw = True

    def updateEntity(self, entity, scene):

        #todo -- update to use scene surface...

        # set clipping rectangle
        cameraComponent = entity.getComponent('camera')
        cameraRect = cameraComponent.rect
        clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
        scene.surface.set_clip(clipRect)

        # zoom
        if entity.hasComponent('intention'):
            intentionComponent = entity.getComponent('intention')
            if intentionComponent.zoomIn:
                cameraComponent.zoomLevel = min(4, cameraComponent.zoomLevel+0.01)
            if intentionComponent.zoomOut:
                # only zoom out if there's more of the world to see
                newZoomLevel = cameraComponent.zoomLevel-0.01
                if (scene.world.map.w_real * newZoomLevel >= cameraRect.w - 10) or (scene.world.map.h_real * newZoomLevel >= cameraRect.h - 10):
                    cameraComponent.zoomLevel = newZoomLevel

        # update camera if tracking an entity
        if cameraComponent.entityToTrack is not None:

            trackedEntity = cameraComponent.entityToTrack

            currentX = cameraComponent.worldX
            currentY = cameraComponent.worldY

            trackedEntityPosition = trackedEntity.getComponent('position')

            targetX = trackedEntityPosition.rect.x + trackedEntityPosition.rect.w/2
            targetY = trackedEntityPosition.rect.y + trackedEntityPosition.rect.h/2

            cameraComponent._updateWorldPosition((currentX * 0.95) + (targetX * 0.05), (currentY * 0.95) + (targetY * 0.05), scene)

        # calculate offsets
        offsetX = cameraRect.x + cameraRect.w/2 - (cameraComponent.worldX * cameraComponent.zoomLevel)
        offsetY = cameraRect.y + cameraRect.h/2 - (cameraComponent.worldY * cameraComponent.zoomLevel)

        angle = 0
        # add camera shake
        if entity.trauma is not None:
            offsetX += (entity.trauma ** 3) * (random.random()*2-1) * 20 * cameraComponent.zoomLevel
            offsetY += (entity.trauma ** 3) * (random.random()*2-1) * 20 * cameraComponent.zoomLevel
            angle += (entity.trauma ** 3) * (random.random()*2-1) * 30 * cameraComponent.zoomLevel

        # fill camera background
        scene.surface.fill(cameraComponent.bgColour)

        # draw level background
        if scene.world.map is not None:

            worldRect = pygame.Rect(
                0 + offsetX,
                0 + offsetY,
                scene.world.map.w_real * cameraComponent.zoomLevel,
                scene.world.map.h_real * cameraComponent.zoomLevel)
            pygame.draw.rect(scene.surface, DARK_GREY, worldRect)

            # render map images behind map
            for img in scene.world.map.mapImages:

                if img.z < 0:

                    # there's no parallax for images behind the map

                    img.draw(scene.surface,
                        (img.x * cameraComponent.zoomLevel) + offsetX,
                        (img.y * cameraComponent.zoomLevel) + offsetY,
                        cameraComponent.zoomLevel) 

        # render map
        if scene.world.map is not None:
            scene.world.map.draw(scene.surface, offsetX, offsetY, cameraComponent.zoomLevel)

        # render entities
        for e in scene.world.entities:
            if e.hasComponent('imagegroups'):
                igComp = e.getComponent('imagegroups')
                p = e.getComponent('position')
                if e.state in igComp.animationList:
                    s = e.state
                    a = igComp.animationList[s]
                    a.draw(scene.surface,
                        (p.rect.x * cameraComponent.zoomLevel) + offsetX,
                        (p.rect.y * cameraComponent.zoomLevel) + offsetY,
                        e.direction == 'left', False, cameraComponent.zoomLevel, igComp.alpha, igComp.hue)

        # render emotes
        for e in scene.world.entities:
            if e.hasComponent('emote'):
                emote = e.getComponent('emote')
                pos = e.getComponent('position')
                emote.draw(scene.surface,
                    ((pos.rect.x + (pos.rect.w/2)) * cameraComponent.zoomLevel) + offsetX,
                    (pos.rect.y * cameraComponent.zoomLevel) + offsetY,
                    cameraComponent.zoomLevel)

        # render text
        for e in scene.world.entities:
            if e.hasComponent('text'):# text is not None:
                txt = e.getComponent('text')
                pos = e.getComponent('position')
                txt.draw(scene.surface, (pos.rect.x * cameraComponent.zoomLevel) + offsetX, (pos.rect.y * cameraComponent.zoomLevel)+ offsetY)

        # particle emitter particles
        for e in scene.world.entities:
            if e.hasComponent('emitter'): #particle_emitter:
                prt = e.getComponent('emitter')
                for p in prt.particles:
                    pygame.draw.circle(scene.surface, p.colour, ((p.pos[0]*cameraComponent.zoomLevel)+offsetX, (p.pos[1]*cameraComponent.zoomLevel)+offsetY), p.size * cameraComponent.zoomLevel)

        # render map images infront of map
        #if engine.world.map is not None:
        #    for img in engine.world.map.mapImages:

        #        if img.z >= 0:

        #            if img.parallaxX:
        #                parallaxOffsetX = ((entity.camera.worldX - img.x) * ( (img.z*-1) * 0.2))
        #            else:
        #                parallaxOffsetX = 0
                    
        #            if img.parallaxY:
          #              parallaxOffsetY = ((entity.camera.worldY - img.y) * ( (img.z*-1) * 0.2))
         #           else:
         #               parallaxOffsetY = 0

        #            img.draw(screen,
        #                (img.x * entity.camera.zoomLevel) + offsetX + parallaxOffsetX,
        #                (img.y * entity.camera.zoomLevel) + offsetY + parallaxOffsetY,
        #                entity.camera.zoomLevel)          

        # render text
        #for e in engine.world.entities:
        #    if e.text is not None:
        #        e.text.draw(screen, (e.position.rect.x * entity.camera.zoomLevel) + offsetX, (e.position.rect.y * entity.camera.zoomLevel)+ offsetY)

        # entity HUD

        # score
        #if entity.score is not None:
        #    screen.blit(utils.coin0, (entity.camera.rect.x + 10, entity.camera.rect.y + 10))
        #    engine.drawText(screen, str(entity.score.score), entity.camera.rect.x + 50, entity.camera.rect.y + 10, WHITE, 255)

        # lives
        #if entity.battle is not None:
        #    for l in range(entity.battle.lives):
        #        screen.blit(utils.heart_image, (entity.camera.rect.x + 200 + (l*50),entity.camera.rect.y + 10))

        # unset clipping rectangle
        scene.surface.set_clip(None)

        # update zoom
        if cameraComponent.zoomPerFrame != 0:
            cameraComponent.zoomLevel += cameraComponent.zoomPerFrame
            if abs(cameraComponent.zoomLevel - cameraComponent.targetZoom) < 0.01 :
                cameraComponent.zoomPerFrame = 0
    
        # update position
        # x
        if cameraComponent.movementPerFrameX != 0:
            cameraComponent.worldX += cameraComponent.movementPerFrameX
            if abs(cameraComponent.worldX - cameraComponent.targetX) < 0.1 :
                cameraComponent.movementPerFrameX = 0
        # y
        if cameraComponent.movementPerFrameY != 0:
            cameraComponent.worldY += cameraComponent.movementPerFrameY
            if abs(cameraComponent.worldY - cameraComponent.targetY) < 0.1 :
                cameraComponent.movementPerFrameY = 0



