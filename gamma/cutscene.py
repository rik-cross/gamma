from .utils import drawRect
from .colours import *
from math import ceil

def delay(amount):
    pass

class Cutscene:

    def __init__(self):

        self.actionList = []
        self.actionIndex = 0
        self.fadePercentage = 0
        self.inOutDuration = 60
        self.colour = BLACK
        self.status = 'in'

        self.currentDelay = 0

    def setDelay(self, amount):
        self.currentDelay = amount

    def advance(self):
        self.actionIndex += 1

    def reset(self):
        self.actionIndex = 0
        self.fadePercentage = 0
        self.status = 'in'

    def update(self, scene):
        if self.status == 'in':
            self.fadePercentage = min(100, self.fadePercentage+(100/self.inOutDuration))
            if self.fadePercentage == 100:
                self.status = 'do'

        if self.status == 'out':
            self.fadePercentage = max(0, self.fadePercentage-(100/self.inOutDuration))
            if self.fadePercentage == 0:
                scene.cutscene = None

        if self.status == 'do':

            if len(self.actionList) > self.actionIndex:

                if self.currentDelay == 0:
                    self.actionList[self.actionIndex]()
                if self.currentDelay == 0:
                    self.advance()
                
                if self.currentDelay > 0:
                    self.currentDelay -= 1
                    if self.currentDelay == 0:
                        self.advance()

            else:
                self.status = 'out'
                
    def draw(self, scene):
        w = scene.surface.get_rect().w
        h = scene.surface.get_rect().h
        p = self.fadePercentage / 100
        drawRect(scene.surface, 0, 0, w, int(h//10 * p), self.colour)
        drawRect(scene.surface, 0, int(h - (h//10) * p) , w, h//10 * p, self.colour)