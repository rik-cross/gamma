from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionMoveLeft(Transition):

    def draw(self):
        
        self.fromScenes[-1]._draw(position=(windowSize[2] / 100 * self.animationPercentage * -1, 0))
        
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw(position=(windowSize[2] - (windowSize[2] / 100 * self.animationPercentage), 0))
        else:
            for s in self.toScenes:
                s._draw(position=(windowSize[2] - (windowSize[2] / 100 * self.animationPercentage), 0))
