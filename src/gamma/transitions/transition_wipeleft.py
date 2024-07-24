from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionWipeLeft(Transition):
        
    def draw(self):

        self.fromScenes[0]._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw(clippingRect=(0, 0, windowSize[2] / 100 * self.currentPercentage, windowSize[3]))
        else:
            self.toScenes[-1]._draw(clippingRect=(0, 0, windowSize[2] / 100 * self.currentPercentage, windowSize[3]))