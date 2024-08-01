from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionWipeRight(Transition):

    def draw(self):

        self.fromScenes[-1]._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw(clippingRect=(windowSize[2] - (windowSize[2] / 100 * self.animationPercentage), 0, windowSize[2], windowSize[3]))
        else:
            self.toScenes[-1]._draw(clippingRect=(windowSize[2] - (windowSize[2] / 100 * self.animationPercentage), 0, windowSize[2], windowSize[3]))
