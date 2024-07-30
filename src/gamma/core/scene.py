import pygame
import math
import os
import pickle
from .colours import *
from .renderer import Renderer
from ..utils.utils import sortByX, sortByY, sortByZ
from ..gamma import screen, systemManager, sceneManager, windowSize
from ..utils.utils import *
from ..utils.utils import drawRect

# TODO
# - create surface once
# - create updateSceneBwlow()

class Scene:
    
    def __init__(self,
    
        # optional parameters
        menu=None,
        background=None,
        backgroundAlpha=255,

        map=None,
        entities=None,
        velocityForces = None,
        accelerationForces = None,

        data = None
    
    ):
        
        # key to sort
        self.orderKey = sortByZ
        self.orderWhen = 'added' # 'always', 'added' or 'never'

        # store map
        self.map = map

        # create scene entity list
        if entities is None:
            self.entities = []
        else:
            self.entities = entities
        
        # create scene forces dictionary
        if velocityForces is None:
            velocityForces = {}
        if accelerationForces is None:
            accelerationForces = {}
        self.forces = {
            'velocity' : velocityForces,
            'acceleration' : accelerationForces
        }

        # entities to delete
        self.delete = []

        # a flag to mark entities for reordering
        self.reorderEntities = False

        self.cutscene = None
        self.frame = 0
        self.menu = menu
        self.buttons = []

        self.background = background
        self.backgroundAlpha = backgroundAlpha

        self.updateSceneBelow = False
        self.drawSceneBelow = False

        self.cameras = []

        # create the scene surface
        self.surface = pygame.Surface((windowSize.w,windowSize.h), pygame.SRCALPHA)
        self.surface.convert_alpha()

        self.renderer = Renderer(self)

        if data is None:
            self.data = {}
        else:
            self.data = data
        
        self.init()

    def init(self):
        pass

    def setMenu(self, menu, scene):
        self.menu = menu
        self.menu.scene = scene
    
    def addButton(self, button):
        self.buttons.append(button)

    def _onEnter(self):
        if self.menu is not None:
            self.menu.setActiveButton()
        self.onEnter()

    def onEnter(self):
        pass

    def _onExit(self):
        if self.menu is not None:
            self.menu.reset()
        self.onExit()

    def onExit(self):
        pass

    def _update(self):

        # update frame and call scene-specific update method
        self.frame += 1
        self.update()
    
        # update systems
        for sys in systemManager.systems:
            sys._update(self)

        # update cutscene
        if self.cutscene is not None:
            self.cutscene.update(self)

        # update menu
        if self.menu is not None:
            self.menu.update()

        # update buttons
        for b in self.buttons:
            b.update()
        
        # update entities
        for e in self.entities:
            e._update()

        # update entity timed actions
        for e in self.entities:
            for action in e.actions:
                action[0] = max(0, action[0] - 1)
                if action[0] == 0:
                    action[1]()
                    e.actions.remove(action)
        
        # reorder scene entities if required
        if self.orderWhen == 'always' or (self.orderWhen == 'added' and self.reorderEntities):
            self.entities.sort(key = self.orderKey)
            if self.reorderEntities:
                self.reorderEntities = False

        # delete marked entities
        for e in self.entities:
            if e.delete:
                self.entities.remove(e)
        
        #update all cameras
        for camera in self.cameras:

            #from ..components.component_camera import camera
            from ..components.component_position import PositionComponent
            #from ..components.component_trauma import TraumaComponent

            # set clipping rectangle
            #camera = entity.getComponent(camera)
            cameraRect = camera.rect

            # update camera if tracking an entity
            if camera.entityToTrack is not None:

                trackedEntity = camera.entityToTrack

                currentX = camera.sceneX
                currentY = camera.sceneY

                trackedEntityPosition = trackedEntity.getComponent(PositionComponent)

                targetX = trackedEntityPosition.rect.x + trackedEntityPosition.rect.w/2
                targetY = trackedEntityPosition.rect.y + trackedEntityPosition.rect.h/2

                camera._updateWorldPosition((currentX * 0.95) + (targetX * 0.05), (currentY * 0.95) + (targetY * 0.05), self)

            # calculate offsets
            offsetX = cameraRect.x + cameraRect.w/2 - (camera.sceneX * camera.zoomLevel)
            offsetY = cameraRect.y + cameraRect.h/2 - (camera.sceneY * camera.zoomLevel)

            # TODO
            angle = 0
            # add camera shake
            #if entity.hasComponent(TraumaComponent):
            #    tc = entity.getComponent(TraumaComponent)
            #    offsetX += (tc.traumaLevel ** 3) * (random.random()*2-1) * 20 * camera.zoomLevel
            #    offsetY += (tc.traumaLevel ** 3) * (random.random()*2-1) * 20 * camera.zoomLevel
            #    angle += (tc.traumaLevel ** 3) * (random.random()*2-1) * 30 * camera.zoomLevel

            # update zoom
            camera._z = camera.zoomLevel
            if camera.zoomPerFrame != 0:
                camera.zoomLevel += camera.zoomPerFrame
                if abs(camera.zoomLevel - camera.targetZoom) < 0.01 :
                    camera.zoomPerFrame = 0
        
            # update position

            # x
            camera._x = offsetX
            if camera.movementPerFrameX != 0:
                camera.sceneX += camera.movementPerFrameX
                if abs(camera.sceneX - camera.targetX) < 0.1 :
                    camera.movementPerFrameX = 0

            # y
            camera._y = offsetY
            if camera.movementPerFrameY != 0:
                camera.sceneY += camera.movementPerFrameY
                if abs(camera.sceneY - camera.targetY) < 0.1 :
                    camera.movementPerFrameY = 0
            
        # update scene below if required
        if self.updateSceneBelow:
            sceneManager.getSceneBelow(self)._update()

    # TODO
    # pass position, clip rect, alpha, ...
    def _draw(self, position=(0,0), clippingRect=None):

        # ** BUG **
        # scene is set before window size is changed
        if pygame.Surface.get_width(self.surface) > windowSize[2] or pygame.Surface.get_height(self.surface) > windowSize[3]:
            self.surface = pygame.Surface((windowSize[2], windowSize[3]))
            self.surface.convert_alpha()

        # draw background (colour or image)
        if self.background is not None:
            if type(self.background) is pygame.Color:
                self.surface.fill(self.background)
            else:
                self.background.draw(self.surface)

        # draw scene below if requested
        if self.drawSceneBelow:
            sceneManager.getSceneBelow(self)._draw()

        # draw scene images behind
        if self.map is not None and self.map.mapImages is not None:
            for i in self.map.mapImages:
                if i.z < 1:
                    self.renderer.add(i, scene=False)

        # draw map
        if self.map is not None:
            self.map.draw(self)

        # draw systems, which send to the renderer
        for sys in systemManager.systems:
            sys._draw(self)

        # draw scene images in front
        if self.map is not None and self.map.mapImages is not None:
            for i in self.map.mapImages:
                if i.z >= 1:
                    self.renderer.add(i, scene=False)

        # draw everything that was sent to the render
        self.renderer.draw()
        self.renderer.flush()

        # draw the cutscene
        if self.cutscene is not None:
            self.cutscene.draw(self)

        # call the scene-specific draw method
        self.draw()

        # draw the menu
        if self.menu is not None:
            self.menu.draw()

        # draw buttons
        for b in self.buttons:
            b.draw(self.surface)              

        # draw the (optionally clipped) scene
        if clippingRect is not None:
            screen.set_clip(clippingRect)
        screen.blit(self.surface, position)
        if clippingRect is not None:
            screen.set_clip()

    def update(self):
        pass

    def draw(self):
        pass

    def addVelocityForce(self, name, force):
        self.forces['velocity'][name] = force

    def addAccelerationForce(self, name, force):
        self.forces['acceleration'][name] = force
    
    def removeForce(self, name):
        if name in self.forces['velocity']:
            del self.forces['velocity'][name]
        if name in self.forces['acceleration']:
            del self.forces['acceleration'][name]

    # entity methods

    def addEntity(self, entity):
        self.entities.append(entity)
        entity.onAddedToScene()
        self.reorderEntities = True
    
    def deleteEntity(self, entity):
        entity.onRemovedFromScene()
        self.entities.remove(entity)
    
    def deleteEntityByID(self, ID):
        for e in self.entities:
            if e.ID == ID:
                self.deleteEntity(e)

    def getEntitiesByTag(self, tag, *otherTags):
        from ..components.component_tags import TagsComponent
        entityList = []
        for e in self.entities:
            if e.getComponent(TagsComponent).has(tag, *otherTags):
                entityList.append(e)
        return entityList

    def getEntityByID(self, entityID):
        for e in self.entities:
            if e.ID == entityID:
                return e
        return None
    
    def getEntitiesWithComponent(self, *componentTypes):
        entityList = []
        for e in self.entities:
            if e.hasComponent(*componentTypes):
                entityList.append(e)
        return entityList
    
    def clear(self):
        self.entities = []
        self.map = None

    # map methods

    def setMap(self, map):
        self.map = map
    
    def loadMap(self, filename):
        filename = os.path.abspath(filename)
        map =  pickle.load( open( filename, "rb" ) )
        map.editorMode = False
        return map

    def saveMap(self, map, filename):
        map.editorMode = False
        filename = os.path.abspath(filename)
        pickle.dump( map, open( filename, "wb" ) )
