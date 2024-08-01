import pygame
from ..gamma import sceneManager, windowSize, screen
from ..core.colours import BLACK
from ..core.transition import Transition

class TransitionBlack(Transition):

    def init(self):
        self.frameDuration /= 2

    def draw(self):

        if self.currentPercentage < 50:
            self.fromScenes[-1]._draw()
        else:
            if len(self.toScenes) == 0:
                if len(sceneManager.scenes) > len(self.fromScenes):
                    sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
            else:
                self.toScenes[-1]._draw()

        # fade overlay
        overlay = pygame.Surface((windowSize.w, windowSize.h))
        alpha = int(abs((255 - ((255/50)*self.animationPercentage))))
        overlay.set_alpha(255 - alpha)
        overlay.fill(BLACK)
        screen.blit(overlay, (0,0))