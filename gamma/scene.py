import pygame
import math
from .engine import sceneManager
from .engine import screen
from .engine import World
from .engine import System

class Scene:
    
    def __init__(self):

        self.world = World()

        self.menu = None
        self.n = ''
        self.minAlpha = 0
        self.maxAlpha = 255
        self.resetEffects()

        self.init()
    def init(self):
        pass

    def resetEffects(self):
        self.currentAlphaPercentage = 100
        self.widthPercentage = 100
        self.heightPercentage = 100
        self.leftPercentage = 0
        self.topPercentage = 0

    def setMenu(self, menu, scene):
        self.menu = menu
        self.menu.scene = scene
    
    def _onEnter(self):
        self.onEnter()
    def onEnter(self):
        pass

    def _onExit(self):
        if self.menu is not None:
            self.menu.reset()
        self.onExit()
    def onExit(self):
        pass
    
    def _input(self):
        self.input()

    def _update(self):
        
        self.update()
        
        for sys in System.systems:
            if not sys.requiresDraw:
                sys.update(self)

        if self.menu is not None:
            self.menu.update()

    def _draw(self):

        w = math.ceil(pygame.display.get_surface().get_size()[0] / 100 * self.widthPercentage)
        h = math.ceil(pygame.display.get_surface().get_size()[1] / 100 * self.heightPercentage)
        self.surface = pygame.Surface((w,h))

        a = math.ceil((self.maxAlpha - self.minAlpha) / 100 * self.currentAlphaPercentage)

        x = math.ceil(pygame.display.get_surface().get_size()[0] / 100 * self.leftPercentage)
        y = math.ceil(pygame.display.get_surface().get_size()[1] / 100 * self.topPercentage)
        
        #print(self.n, x)

        self.draw()

        for sys in System.systems:
            if sys.requiresDraw:
                sys.update(self)
        
        if self.menu is not None:
            self.menu.draw()

        self.surface.set_alpha(a)
        screen.blit(self.surface, (x,y))

    def input(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

    def getSceneBelow(self): # TODO
        #s = self
        #print(s in sceneManager.scenes)
        #i = sceneManager.scenes.index(self)
        return sceneManager.scenes# ........