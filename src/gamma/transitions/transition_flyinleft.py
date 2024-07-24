from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionFlyInLeft(Transition):

    def draw(self):

        for s in self.fromScenes:
            s._draw()

        # fixes a bug where the toScenes are shown for the first frame
        if self.currentPercentage == 0:
            return

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw(position=(-windowSize[2] + (windowSize[2] / 100 * self.currentPercentage), 0))
        else:
            for s in self.toScenes:
                s._draw(position=(-windowSize[2] + (windowSize[2] / 100 * self.currentPercentage), 0))
