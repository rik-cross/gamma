import pygame
import math
from .gamma import screen, systemManager
from .world import World

class Scene:
    
    def __init__(self, world=World(), menu=None):
        self.frame = 0
        self.world = world
        self.menu = menu
        self.buttons = []
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
    
    def addButton(self, button):
        self.buttons.append(button)

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

        self.frame += 1
        self.update()
    
        for sys in systemManager.systems:
            if not sys.requiresDraw:
                sys.update(self)

        if self.menu is not None:
            self.menu.update()

        for b in self.buttons:
            b.update()

    def _draw(self):

        # calculate the scene size
        w = math.ceil(pygame.display.get_surface().get_size()[0] / 100 * self.widthPercentage)
        h = math.ceil(pygame.display.get_surface().get_size()[1] / 100 * self.heightPercentage)
        self.surface = pygame.Surface((w,h))
        
        # call the scene-specific draw method
        self.draw()

        # update systems that require a draw call
        for sys in systemManager.systems:
            if sys.requiresDraw:
                sys.update(self)
        
        # draw the menu
        if self.menu is not None:
            self.menu.draw()

        # draw buttons
        for b in self.buttons:
            b.draw(self.surface)

        # calculate the scene position and transparency
        a = math.ceil(self.maxAlpha / 100 * self.currentAlphaPercentage)
        x = math.ceil(pygame.display.get_surface().get_size()[0] / 100 * self.leftPercentage)
        y = math.ceil(pygame.display.get_surface().get_size()[1] / 100 * self.topPercentage)

        # draw the scene
        self.surface.set_alpha(a)
        screen.blit(self.surface, (x,y))

    def input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
