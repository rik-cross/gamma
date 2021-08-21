import pygame
from .system import System
from .colours import *
import random

class CameraSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['camera']
        self.requiresDraw = True

    def updateEntity(self, entity, scene):

        # set clipping rectangle
        cameraComponent = entity.getComponent('camera')
        cameraRect = cameraComponent.rect
        clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
        scene.surface.set_clip(clipRect)

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
        if cameraComponent.bgColour is not None:
            scene.surface.fill(cameraComponent.bgColour)

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
            # map grid lines
            if scene.world.map.drawGrid:
                # columns
                for c in range(0,scene.world.map.MAX_MAPSIZE*scene.world.map.tileSize,scene.world.map.tileSize):
                    pygame.draw.line(scene.surface, LIGHT_GREY, (c*cameraComponent.zoomLevel+offsetX,0*cameraComponent.zoomLevel+offsetY), (c*cameraComponent.zoomLevel+offsetX,scene.world.map.MAX_MAPSIZE*scene.world.map.tileSize*cameraComponent.zoomLevel+offsetY))
                # rows
                for r in range(0,scene.world.map.MAX_MAPSIZE*scene.world.map.tileSize,scene.world.map.tileSize):
                    pygame.draw.line(scene.surface, LIGHT_GREY, (0*cameraComponent.zoomLevel+offsetX,r*cameraComponent.zoomLevel+offsetY), (scene.world.map.MAX_MAPSIZE*scene.world.map.tileSize*cameraComponent.zoomLevel+offsetX,r*cameraComponent.zoomLevel+offsetY))

        # render entities
        for e in scene.world.entities:
            if e.hasComponent('imagegroups'):
                igComp = e.getComponent('imagegroups')
                p = e.getComponent('position')
                if igComp.current is not None:
                    s = igComp.current
                    a = igComp.animationList[s]

                    # use position angle to work out image flips
                    hFlip = False
                    vFlip = False
                    if p.rotationStyle == 'leftRight':
                        if p.angle == 270:
                            hFlip = True
                    a.draw(scene.surface,
                        (p.rect.x * cameraComponent.zoomLevel) + offsetX,
                        (p.rect.y * cameraComponent.zoomLevel) + offsetY,
                        hFlip, vFlip, cameraComponent.zoomLevel, igComp.alpha, igComp.hue)

        # render emotes
        for e in scene.world.entities:
            if e.hasComponent('emote', 'position'):
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



