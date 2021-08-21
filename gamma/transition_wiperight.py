from .transition import Transition
from .gamma import sceneManager

class TransitionWipeRight(Transition):

    def init(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)].widthPercentage = 0
        else:
            for s in self.toScenes:
                s.widthPercentage = 0

    def update(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)].widthPercentage = self.currentPercentage
        else:
            for s in self.toScenes:
                s.widthPercentage = self.currentPercentage
                
    def draw(self):

        self.fromScenes[-1]._draw()

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            self.toScenes[-1]._draw()
