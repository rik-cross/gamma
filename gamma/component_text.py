from .ui_text import *
from .colours import *
import gamma as engine
import pygame
from .colours import *

class Text:

    def __init__(self, text):
        self.key = 'text'
        self.text = text

        # lifetimes are 'timed', 'always' and 'press'
        self.lifetime = 'always'
        
        # delay used for 'tick' appearance
        self.delay = 5
        # fade used for 'fade' type
        self.fadeAmount = 255 # 0 to 255

        self.delayTimer = self.delay

        self.colour = WHITE

        # for 'timed'
        self.finalTimer = 300
        # for 'press'
        self.button = None
        
        self.width = 20

        self.sound = None

        # internal variables
        self.textList = []
        self.destroy = False

        self.overhead = True

        self.enterOrExit = 'enter'

        row = ''
        for char in self.text:
            row = row + char
            if len(row) >= self.width and char == ' ':
                self.textList.append(row[:-1])
                row = ''
        if len(row) > 0:
            self.textList.append(row)

        # set for 'appear' initially
        self.setType('appear')
    
    def startExit(self):
        self.enterOrExit = 'exit'

    def setType(self, type):
        # types are 'appear', 'tick' or 'fade'
        self.type = type
        if self.type == 'appear':
            self.finished = True
            self.index = self.width
            self.row = len(self.textList)
            self.fadeAmount = 255
        if self.type == 'tick':
            self.finished = False
            self.index = 0
            self.row = 0
            self.fadeAmount = 255
        if self.type == 'fade':
            self.fadeAmount = 0
            self.finished = False
            self.index = self.width
            self.row = len(self.textList)

    def setLifetime(self, lifetime):
        self.lifetime = lifetime

    def update(self):

        if self.type == 'appear':
            pass

        if self.type == 'tick' and self.enterOrExit == 'enter':
            if not self.finished:
                self.delayTimer -= 1
                if self.delayTimer <= 0:
                    self.delayTimer = self.delay
                    self.index += 1
                    if self.sound:
                        engine.soundManager.playSound(self.sound, engine.soundManager.soundVolume / 2)
                    if self.index >= len(self.textList[self.row]):
                        self.index = 0
                        self.row += 1
                        if self.row >= len(self.textList):
                            #if self.autoFinish:
                            self.finished = True
                            #else:
                            #    # if button pressed for entity:
                            #    pass

        if self.type == 'fade' and self.enterOrExit == 'enter':
            self.fadeAmount = min(self.fadeAmount+2, 255)
            if self.fadeAmount == 255:
                self.finished = True

        if self.finished and self.enterOrExit == 'enter':

            if self.lifetime == 'always':
                pass

            if self.lifetime == 'timed':
                #if self.autoFinish is True:
                self.finalTimer -= 1
                if self.finalTimer <= 0:
                    
                    #todo -- don't destroy, instead should fade out again! -- use inOut var?
                    #self.destroy = True
                    self.enterOrExit = 'exit'

        # can press regardless of progress
        if self.lifetime == 'press':
            if self.button is not None:
                if engine.inputManager.isPressed(self.button):
                    #self.destroy = True
                    self.enterOrExit = 'exit'
                        
        if self.enterOrExit == 'exit':

            self.fadeAmount = max(self.fadeAmount - 2, 0)
            if self.fadeAmount == 0:
                self.destroy = True

    def draw(self, screen, x, y):        
        rows = 30 * len(self.textList)

        for i,l in enumerate(self.textList):
            if i == self.row:
                drawText(l[0:self.index], x, y-10-rows+(i*30), self.colour, self.fadeAmount)
            elif i < self.row:
                drawText(l, x, y-10-rows+(i*30), self.colour, self.fadeAmount)