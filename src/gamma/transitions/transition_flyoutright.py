from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionFlyOutRight(Transition):

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            for s in self.toScenes:
                s._draw()

        self.fromScenes[-1]._draw(position=(windowSize[2] / 100 * self.animationPercentage, 0))
