import pygame
import math
from .gamma import screen, systemManager, sceneManager, windowSize
from .world import World
from .utils import *
from .colours import *
from .renderer import Renderer
from .utils import drawRect

class Scene:
    
    def __init__(self,
    
        # optional parameters
        world=None,
        menu=None,
        background=None,
        backgroundAlpha=255
    
    ):

        self.world = world
        if self.world is None:
            self.world = World()

        self.cutscene = None
        self.frame = 0
        self.menu = menu
        self.buttons = []
        self.resetEffects()

        self.background = background
        self.backgroundAlpha = backgroundAlpha

        self.drawSceneBelow = False

        self.renderer = Renderer(self)

        self.init()

    def init(self):
        pass

    def resetEffects(self):
        self.widthPercentage = 100
        self.heightPercentage = 100
        self.leftPercentage = 0
        self.topPercentage = 0

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
        
        if self.world is not None:
            self.world._update()
        
    def _draw(self):

        # calculate the scene size
        w = int(windowSize.w / 100 * self.widthPercentage)
        h = int(windowSize.h / 100 * self.heightPercentage)
        
        # create the scene surface
        self.surface = pygame.Surface((w,h), pygame.SRCALPHA)
        if self.backgroundAlpha < 255:
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

        # draw world images behind
        if self.world.map is not None and self.world.map.mapImages is not None:
            for i in self.world.map.mapImages:
                if i.z < 1:
                    self.renderer.add(i, scene=False)

        # draw map
        if self.world.map is not None:
            self.world.map.draw(self)

        # draw systems, which send to the renderer
        for sys in systemManager.systems:
            sys._draw(self)

        # draw world images in front
        if self.world.map is not None and self.world.map.mapImages is not None:
            for i in self.world.map.mapImages:
                if i.z >= 1:
                    self.renderer.add(i, scene=False)

        # draw everything that was sent to the render
        self.renderer.draw()
        self.renderer.flush()

        # calculate the scene position and transparency
        x = math.ceil(pygame.display.get_surface().get_size()[0] / 100 * self.leftPercentage)
        y = math.ceil(pygame.display.get_surface().get_size()[1] / 100 * self.topPercentage)

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

        # draw the scene
        screen.blit(self.surface, (x,y))

    def update(self):
        pass

    def draw(self):
        pass
