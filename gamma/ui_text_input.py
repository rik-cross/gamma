from gamma.rectangle import Rectangle
from .utils import drawBox
from .text import Text
from .gamma import inputManager, entityManager
from .colours import *

keyboard = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

class UITextInput:

    def __init__(self, x=0, y=0, w=100, h=100, keyboard=keyboard, show=True, text='', onComplete=None):
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.keyboard = keyboard
        self.show = show

        self.text = text

        self.cursorX = 0
        self.cursorY = 0

        self.complete = False
        self.onComplete = onComplete

    def update(self):
        
        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').b1):
            self.text = self.text + self.keyboard[self.cursorY][self.cursorX]

        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').b4):
            self.text = self.text[:-1]

        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').b17):
            self.complete = True
            if self.onComplete is not None:
                self.onComplete()
        
        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').up):
            if len(self.keyboard[self.cursorY-1]) > self.cursorX:
                self.cursorY = max(0, self.cursorY - 1)
        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').down):
            if len(self.keyboard)-1 > self.cursorY:
                if len(self.keyboard[self.cursorY+1]) > self.cursorX:
                    self.cursorY = min(len(self.keyboard)-1, self.cursorY + 1)

        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').left):
            self.cursorX = max(0, self.cursorX - 1)
        if inputManager.isPressed(entityManager.getEntitiesByTag('player1')[0].getComponent('input').right):
            self.cursorX = min(len(self.keyboard[self.cursorY])-1, self.cursorX + 1)

    def draw(self, surface):

        for c in range(len(self.keyboard)):
            for r in range(len(self.keyboard[c])):
                #print(self.keyboard[c][r])
                Rectangle(self.x+r*32, self.y+c*32, 32, 32, colour=DARK_GREY).draw(surface)
                drawBox(surface, self.x+r*32, self.y+c*32, 32, 32, BLACK)
                Text(self.keyboard[c][r],self.x+r*32+10, self.y+c*32).draw(surface)
                
                Rectangle(self.x, self.y + 32*len(self.keyboard), 32*10, 32*2, colour=BLACK).draw(surface)
        
                drawBox(surface, self.x+self.cursorX*32, self.y+self.cursorY*32, 32, 32, WHITE)

                Text(self.text,self.x+10, self.y + 32*len(self.keyboard) + 32, vAlign='middle').draw(surface)

