from ..gamma import sceneManager
from ..core.transition import Transition

class TransitionFlyInLeft(Transition):

    def init(self):
        for s in self.toScenes:
            s.leftPercentage = -100

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)].leftPercentage = -100 + self.currentPercentage
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
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            for s in self.toScenes:
                s._draw()
