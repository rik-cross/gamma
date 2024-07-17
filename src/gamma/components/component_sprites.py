from ..core.component import Component

class SpritesComponent(Component):

    def __init__(self, key=None, sprite=None):
        self.current = None
        self.spriteList = {}
        self.alpha = 255
        self.hue = None
        self.playing = True
        if key is not None and sprite is not None:
            self.add(key, sprite)
    
    def setHue(self, hue):
        self.hue = hue

    def getCurrentSprite(self):
        if self.spriteList == {} or self.current is None:
            return None
        return self.spriteList[self.current]

    def add(self, state, sprite):
        self.spriteList[state] = sprite
    
    def pause(self):
        self.playing = False

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
        if self.current is not None:
            self.spriteList[self.current].reset()