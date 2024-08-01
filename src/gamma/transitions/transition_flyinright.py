from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionFlyInRight(Transition):

    def draw(self):
        
        self.fromScenes[-1]._draw()
        
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw(position=(windowSize[2] - (windowSize[2] / 100 * self.animationPercentage), 0))
        else:
            for s in self.toScenes:
                s._draw(position=(windowSize[2] - (windowSize[2] / 100 * self.animationPercentage), 0))
