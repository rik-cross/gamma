import pygame

class Renderer:

    def __init__(self, scene):

        # list of items to render
        self.renderable = []
        # a renderer is attached to a scene
        self.scene = scene
    
    # adds a renderable object to the renderer
    def add(self, r):
        self.renderable.append(r)
    
    # removes all renderable objects from the renderer
    def flush(self):
        self.renderable = []

    def draw(self):

        #
        # draw all renderable objects, for all cameras
        #

        # iterate over all cameras
        entitiesWithCamera = self.scene.world.getEntitiesWithComponent('camera')
        for e in entitiesWithCamera:

            # get the camera component
            camera = e.getComponent('camera')
                
            # set clipping rectangle
            cameraRect = camera.rect
            clipRect = pygame.Rect(cameraRect.x, cameraRect.y, cameraRect.w, cameraRect.h)
            self.scene.surface.set_clip(clipRect)

            # fill camera background
            if camera.bgColour is not None:
                self.scene.surface.fill(camera.bgColour)

            # draw each renderable, transformed for the camera
            for r in self.renderable:
                r.draw(self.scene.surface, camera._x, camera._y, camera._z)
            
            # unset clipping rectangle
            self.scene.surface.set_clip(None)
