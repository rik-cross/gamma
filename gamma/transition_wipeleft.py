from .transition import Transition
from .gamma import sceneManager

class TransitionWipeLeft(Transition):

    def update(self):

        for s in self.fromScenes:
            s.widthPercentage = 100 - self.currentPercentage
        
    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            self.toScenes[-1]._draw()

        self.fromScenes[0]._draw()
