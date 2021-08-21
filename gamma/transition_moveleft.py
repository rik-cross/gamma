from .transition import Transition
from .gamma import sceneManager

class TransitionMoveLeft(Transition):

    def init(self):
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)].leftPercentage = 100
        else:
            for s in self.toScenes:
                s.leftPercentage = 100

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)].leftPercentage = max(0,100 - self.currentPercentage - 1)
        else:
            for s in self.toScenes:
                s.leftPercentage = 100 - self.currentPercentage
        
        for s in self.fromScenes:
            s.leftPercentage = 0 - self.currentPercentage

    def draw(self):
        
        self.fromScenes[-1]._draw()
        
        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            for s in self.toScenes:
                s._draw()
