import pygame
from .colours import *
from .gamma import sceneManager, screen

class Transition:

    def __init__(self, fromScenes, toScenes, frameDuration=30):
        self.fromScenes = fromScenes
        self.toScenes = toScenes
        self.frameDuration = frameDuration
        self.currentPercentage = 0

        self.resetAllSceneEffects()
        self.init()

    def init(self):
        pass

    def resetAllSceneEffects(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].resetEffects()
        else:
            for s in self.toScenes:
                s.resetEffects()
        
        for s in self.fromScenes:
            s.resetEffects()
        
        for s in sceneManager.scenes:
            s.resetEffects()

    def _onComplete(self):

        self.resetAllSceneEffects()

        if len(self.toScenes) == 0:
                sceneManager.pop()
        else:
            for s in self.toScenes:
                sceneManager.push(s)

        self.onComplete()

    def onComplete(self):
        pass

    def _update(self):

        self.currentPercentage = min(100, self.currentPercentage+(100/self.frameDuration))

        for fs in self.fromScenes:
            fs._update()

        for ts in self.toScenes:
            ts._update()

        if self.currentPercentage == 100:
            sceneManager.transition = None
            self._onComplete()

        self.update()
    def update(self):
        pass

    def _draw(self):
        self.draw()
    def draw(self):
        pass

class TransitionNone(Transition):

    def init(self):
        self.currentPercentage = 100

    def draw(self):

        for s in self.fromScenes:
            s._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

class TransitionBlack(Transition):

    def draw(self):

        if self.currentPercentage < 50:
            sceneManager.getTopScene()._draw()
            for s in self.fromScenes:
                s._draw()
        else:
            if len(self.toScenes) == 0:
                if len(sceneManager.scenes) > 1:
                    sceneManager.scenes[-2]._draw()
            else:
                for s in self.toScenes:
                    s._draw()

        # fade overlay
        overlay = pygame.Surface(pygame.display.get_surface().get_size())
        alpha = int(abs((255 - ((255/50)*self.currentPercentage))))
        overlay.set_alpha(255 - alpha)
        overlay.fill(BLACK)
        screen.blit(overlay, (0,0))

class TransitionFade(Transition):

    def init(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].currentAlphaPercentage = 0
        else:
            for s in self.toScenes:
                s.currentAlphaPercentage = 0    

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].currentAlphaPercentage = self.currentPercentage
        else:
            for s in self.toScenes:
                s.currentAlphaPercentage = self.currentPercentage

    def draw(self):
        
        for s in self.fromScenes:
            s._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

class TransitionWipeRight(Transition):

    def init(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].widthPercentage = 0
        else:
            for s in self.toScenes:
                s.widthPercentage = 0

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].widthPercentage = self.currentPercentage
                #print(sceneManager.scenes[-2].widthPercentage)
        else:
            for s in self.toScenes:
                s.widthPercentage = self.currentPercentage
                

    def draw(self):
        
        for s in self.fromScenes:
            s._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

class TransitionWipeLeft(Transition):

    def update(self):

        for s in self.fromScenes:
            s.widthPercentage = 100 - self.currentPercentage

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()
        
        for s in self.fromScenes:
            s._draw()

class TransitionFlyOutRight(Transition):

    def update(self):

        for s in self.fromScenes:
            s.leftPercentage = self.currentPercentage

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

        for s in self.fromScenes:
            s._draw()

class TransitionFlyOutLeft(Transition):    

    def update(self):

        for s in self.fromScenes:
            s.leftPercentage = 0 - self.currentPercentage

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()
        
        for s in self.fromScenes:
            s._draw()

class TransitionFlyInRight(Transition):

    def init(self):
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = 100
        else:
            for s in self.toScenes:
                s.leftPercentage = 100

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = 100 - self.currentPercentage - 1
        else:
            for s in self.toScenes:
                s.leftPercentage = 100 - self.currentPercentage

    def draw(self):
        
        for s in self.fromScenes:
            s._draw()
        
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

class TransitionFlyInLeft(Transition):

    def init(self):
        for s in self.toScenes:
            s.leftPercentage = -100

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = -100 + self.currentPercentage
        else:
            for s in self.toScenes:
                s.leftPercentage = -100 + self.currentPercentage

    def draw(self):

        for s in self.fromScenes:
            s._draw()

        # fixes a bug where the toScenes are shown for the first frame
        if self.currentPercentage == 0:
            return

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

class TransitionMoveLeft(Transition):

    def init(self):
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = 100
        else:
            for s in self.toScenes:
                s.leftPercentage = 100

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = 100 - self.currentPercentage - 1
        else:
            for s in self.toScenes:
                s.leftPercentage = 100 - self.currentPercentage
        
        for s in self.fromScenes:
            s.leftPercentage = 0 - self.currentPercentage

    def draw(self):
        
        for s in self.fromScenes:
            s._draw()
        
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()

class TransitionMoveRight(Transition):

    def init(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = -100
        else:
            for s in self.toScenes:
                s.leftPercentage = -100

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].leftPercentage = -100 + self.currentPercentage - 1
        else:
            for s in self.toScenes:
                s.leftPercentage = -100 + self.currentPercentage
        
        for s in self.fromScenes:
            s.leftPercentage = self.currentPercentage

    def draw(self):
        
        for s in self.fromScenes:
            s._draw()
        
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2]._draw()
        else:
            for s in self.toScenes:
                s._draw()