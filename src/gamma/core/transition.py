from ..gamma import sceneManager
from ..utils.easing_functions import easeLinear

class Transition:

    def __init__(self, fromScenes, toScenes, frameDuration=60, replaceScenes=False, easingFunction = None):
        self.fromScenes = fromScenes
        self.toScenes = toScenes
        self.frameDuration = frameDuration
        self.currentPercentage = 0
        self.animationPercentage = 0
        self.replaceScenes = replaceScenes
        if easingFunction is None:
            self.easingFunction = easeLinear
        else:
            self.easingFunction = easingFunction
        self.init()

    def init(self):
        pass

    def _onComplete(self):

        if len(self.toScenes) == 0:
            for s in self.fromScenes:
                sceneManager.pop()
        else:
            if self.replaceScenes:
                sceneManager.clear()
            for s in self.toScenes:
                sceneManager.push(s)

        self.onComplete()

    def onComplete(self):
        pass

    def _update(self):

        self.currentPercentage = min(100, self.currentPercentage+(100/self.frameDuration))
        self.animationPercentage = self.easingFunction(self.currentPercentage)

        # update the top of the new scenes,
        # if there is one
        if len(self.toScenes) > 0:
            self.toScenes[-1]._update()

        # update the top scene in the
        # current scene stack
        if len(sceneManager.scenes) > 0:
            sceneManager.getTopScene()._update()

        if self.currentPercentage == 100:
            sceneManager.transition = None
            self._onComplete()

        self.update()

    def update(self):
        pass

    def _draw(self):
        self.draw()
    def draw(self):
        pass
