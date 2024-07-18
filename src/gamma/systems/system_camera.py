import random
from ..core.system import System
from ..core.colours import *

class CameraSystem(System):

    def init(self):
        from ..components.component_camera import CameraComponent
        self.setRequiredComponents(CameraComponent)

    def updateEntity(self, entity, scene):

        from ..components.component_camera import CameraComponent
        from ..components.component_position import PositionComponent
        from ..components.component_trauma import TraumaComponent

        # set clipping rectangle
        cameraComponent = entity.getComponent(CameraComponent)
        cameraRect = cameraComponent.rect

        # update camera if tracking an entity
        if cameraComponent.entityToTrack is not None:

            trackedEntity = cameraComponent.entityToTrack

            currentX = cameraComponent.sceneX
            currentY = cameraComponent.sceneY

            trackedEntityPosition = trackedEntity.getComponent(PositionComponent)

            targetX = trackedEntityPosition.rect.x + trackedEntityPosition.rect.w/2
            targetY = trackedEntityPosition.rect.y + trackedEntityPosition.rect.h/2

            cameraComponent._updateWorldPosition((currentX * 0.95) + (targetX * 0.05), (currentY * 0.95) + (targetY * 0.05), scene)

        # calculate offsets
        offsetX = cameraRect.x + cameraRect.w/2 - (cameraComponent.sceneX * cameraComponent.zoomLevel)
        offsetY = cameraRect.y + cameraRect.h/2 - (cameraComponent.sceneY * cameraComponent.zoomLevel)

        angle = 0
        # add camera shake
        if entity.hasComponent(TraumaComponent):
            tc = entity.getComponent(TraumaComponent)
            offsetX += (tc.traumaLevel ** 3) * (random.random()*2-1) * 20 * cameraComponent.zoomLevel
            offsetY += (tc.traumaLevel ** 3) * (random.random()*2-1) * 20 * cameraComponent.zoomLevel
            angle += (tc.traumaLevel ** 3) * (random.random()*2-1) * 30 * cameraComponent.zoomLevel

        # update zoom
        cameraComponent._z = cameraComponent.zoomLevel
        if cameraComponent.zoomPerFrame != 0:
            cameraComponent.zoomLevel += cameraComponent.zoomPerFrame
            if abs(cameraComponent.zoomLevel - cameraComponent.targetZoom) < 0.01 :
                cameraComponent.zoomPerFrame = 0
    
        # update position

        # x
        cameraComponent._x = offsetX
        if cameraComponent.movementPerFrameX != 0:
            cameraComponent.sceneX += cameraComponent.movementPerFrameX
            if abs(cameraComponent.sceneX - cameraComponent.targetX) < 0.1 :
                cameraComponent.movementPerFrameX = 0

        # y
        cameraComponent._y = offsetY
        if cameraComponent.movementPerFrameY != 0:
            cameraComponent.sceneY += cameraComponent.movementPerFrameY
            if abs(cameraComponent.sceneY - cameraComponent.targetY) < 0.1 :
                cameraComponent.movementPerFrameY = 0
        
        
        
        



