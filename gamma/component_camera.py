import pygame
from .component import Component
from .colours import *

class CameraComponent(Component):

    def __init__(self, x, y, w, h,
        bgColour=None,
        worldX = 0, worldY = 0,
        entityToTrack = None,
        zoomLevel = 1
        ):
        
        self.key = 'camera'
        
        self.rect = pygame.Rect(x,y,w,h)
        self.bgColour = bgColour
        
        self.worldX = worldX
        self.worldY = worldY
        self.entityToTrack = entityToTrack
        self.zoomLevel = zoomLevel

        self.zoomPerFrame = 0
        self.targetZoom = self.zoomLevel

        self.targetX = 0
        self.targetY = 0
        self.movementPerFrameX = 0
        self.movementPerFrameY = 0

        self.clampToWorld=True

        # test
        self._x = 0
        self._y = 0
        self._z = 0
    
    def getTransform(x, y):
        pass # todo
    
    def setZoom(self, level, duration=1):
        if duration < 1:
            return
        self.targetZoom = level
        self.zoomPerFrame = (self.targetZoom - self.zoomLevel) / duration

    def setPosition(self, x, y, duration=1):
        if duration < 1:
            return
        self.entityToTrack = None
        self.targetX = x
        self.targetY = y
        self.movementPerFrameX = (self.targetX - self.worldX) / duration
        self.movementPerFrameY = (self.targetY - self.worldY) / duration

    def _updateWorldPosition(self, x, y, scene):

        newX = x
        newY = y
  
        if scene.world is not None and scene.world.map is not None and self.clampToWorld:

            # calculate x value

            # if world narrower than camera:
            if (self.rect.w) > (scene.world.map.w_real*self.zoomLevel):
                newX = int(scene.world.map.w_real / 2)
            else:
                newX = max(newX, (self.rect.w/self.zoomLevel)/2)
                newX = min(newX, ( ((scene.world.map.w_real) - (self.rect.w/2/self.zoomLevel)) ) )

            # calculate y value

            # if world narrower than camera:
            if self.rect.h > (scene.world.map.h_real*self.zoomLevel):
                newY = int(scene.world.map.h_real / 2)
            else:
                newY = max(newY, (self.rect.h/self.zoomLevel/2))
                newY = min(newY, ( ((scene.world.map.h_real) - (self.rect.h/2/self.zoomLevel)) ) )

        self.worldX = newX
        self.worldY = newY

    def trackEntity(self, entity):
        self.entityToTrack = entity
    
    def goToEntity(self, entity):
        self.entityToTrack = None
        pos = entity.getComponent('position')
        self.worldX = pos.rect.x + (pos.rect.w / 2)
        self.worldY = pos.rect.y + (pos.rect.h / 2)
