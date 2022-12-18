import pygame
from ..core.component import Component
from ..core.colours import *

class CameraComponent(Component):

    def __init__(self,
    
        # required parameters
        x, y,
        w, h,
        
        # optional parameters
        bgColour=None,
        sceneX = 0, sceneY = 0,
        entityToTrack = None,
        zoomLevel = 1,
        clampToMap = True
    
    ):
        
        self.key = 'camera'
        
        self.rect = pygame.Rect(x, y, w, h)
        self.bgColour = bgColour
        
        self.sceneX = sceneX
        self.sceneY = sceneY
        self.entityToTrack = entityToTrack
        self.zoomLevel = zoomLevel

        self.zoomPerFrame = 0
        self.targetZoom = self.zoomLevel

        self.targetX = 0
        self.targetY = 0
        self.movementPerFrameX = 0
        self.movementPerFrameY = 0

        self.clampToWorld = clampToMap

        self._x = 0
        self._y = 0
        self._z = 0
    
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
        self.movementPerFrameX = (self.targetX - self.sceneX) / duration
        self.movementPerFrameY = (self.targetY - self.sceneY) / duration

    # sets the zoom level and position
    # so that the entire map is visible in the camera
    def setFullScreen(self, map):

        # set the camera to the center of the world
        self.sceneX = map.w_real / 2
        self.sceneY = map.h_real / 2
        # set the zoom level
        if (self.rect.width / map.w_real) < (self.rect.height / map.h_real):
            z = self.rect.width / map.w_real
        else:
            z = self.rect.height / map.h_real
        self.zoomLevel = z

    def _updateWorldPosition(self, x, y, scene):

        newX = x
        newY = y

        if scene is not None and scene.map is not None and self.clampToWorld:

            # calculate x value

            # if scene narrower than camera:
            if (self.rect.w) > (scene.map.w_real*self.zoomLevel):
                newX = int(scene.map.w_real / 2)
            else:
                newX = max(newX, (self.rect.w/self.zoomLevel)/2)
                newX = min(newX, ( ((scene.map.w_real) - (self.rect.w/2/self.zoomLevel)) ) )

            # calculate y value

            # if scene narrower than camera:
            if self.rect.h > (scene.map.h_real*self.zoomLevel):
                newY = int(scene.map.h_real / 2)
            else:
                newY = max(newY, (self.rect.h/self.zoomLevel/2))
                newY = min(newY, ( ((scene.map.h_real) - (self.rect.h/2/self.zoomLevel)) ) )

        self.sceneX = newX
        self.sceneY = newY

    def trackEntity(self, entity):
        self.entityToTrack = entity
    
    def goToEntity(self, entity):
        self.entityToTrack = None
        pos = entity.getComponent('position')
        self.sceneX = pos.rect.x + (pos.rect.w / 2)
        self.sceneY = pos.rect.y + (pos.rect.h / 2)
