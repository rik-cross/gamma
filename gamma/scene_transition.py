from .scene import Scene
from .engine import sceneManager

class TransitionScene(Scene):
    def __init__(self, fromScenes, toScenes):
        self.currentPercentage = 0
        self.fromScenes = fromScenes
        self.toScenes = toScenes
        self.menu = None
        self.init()
    def _update(self):
        self.currentPercentage += 2
        if self.currentPercentage >= 100:
            sceneManager.pop()
            for s in self.toScenes:
                sceneManager.push(s)
        for scene in self.fromScenes:
            scene.update()
        if len(self.toScenes) > 0:
            for scene in self.toScenes:
                scene.update()
        else:
            if len(sceneManager.scenes) > 1:
                sceneManager.scenes[-2].update()