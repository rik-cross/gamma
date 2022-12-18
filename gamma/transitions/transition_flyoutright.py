from ..gamma import sceneManager
from ..core.transition import Transition

class TransitionFlyOutRight(Transition):

    def update(self):

        for s in self.fromScenes:
            s.leftPercentage = self.currentPercentage

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            for s in self.toScenes:
                s._draw()

        self.fromScenes[-1]._draw()
