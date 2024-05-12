from ..gamma import sceneManager
from ..core.transition import Transition

class TransitionNone(Transition):

    def init(self):
        self.currentPercentage = 100

    def draw(self):

        for s in self.fromScenes:
            s._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            self.toScenes[-1]._draw()
