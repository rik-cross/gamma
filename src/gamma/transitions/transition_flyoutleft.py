from ..gamma import sceneManager
from ..core.transition import Transition
from ..gamma import windowSize

class TransitionFlyOutLeft(Transition):    

    def draw(self):

        if len(self.toScenes) == 0:
            if len(sceneManager.scenes) > len(self.fromScenes):
                sceneManager.scenes[-2 - (len(self.fromScenes)-1)]._draw()
        else:
            self.toScenes[-1]._draw()
        
        for s in self.fromScenes:
            s._draw(position=(windowSize[2] / 100 * self.currentPercentage * -1, 0))
