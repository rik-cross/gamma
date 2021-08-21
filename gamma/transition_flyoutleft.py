from .transition import Transition
from .gamma import sceneManager


class TransitionFlyOutLeft(Transition):    

    def update(self):

        for s in self.fromScenes:
            s.leftPercentage = 0 - self.currentPercentage

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            self.toScenes[-1]._draw()
        
        for s in self.fromScenes:
            s._draw()
