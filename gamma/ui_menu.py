import pygame
import gamma as engine
from .inputmanager import *

class Menu:
    
    def __init__(self, x, y, buttons=None, direction='vertical', spacing=50):
        
        if buttons is None:
            self.buttons = []
        else:
            self.buttons = buttons
        self.activeButtonIndex = 0
        self.x = x
        self.y = y
        self.direction = direction
        self.spacing = spacing

    def addButton(self, button):
        self.buttons.append(button)
    
    def reset(self):
        self.activeButtonIndex = 0
        for b in self.buttons:
            b.reset()
        if len(self.buttons) > 0:
            self.buttons[0].update(True, False)

    def update(self):
        # update active button based on input
        if engine.inputManager.isPressed(keys.w):
            self.activeButtonIndex = max(0, self.activeButtonIndex - 1)
        if engine.inputManager.isPressed(keys.s):
            self.activeButtonIndex = min(len(self.buttons)-1, self.activeButtonIndex + 1)
        # update buttons in the button group    
        for i in range(len(self.buttons)):
            self.buttons[i].update(self.activeButtonIndex == i, self.activeButtonIndex == i and engine.inputManager.isPressed(keys.enter))

    def draw(self):
        bX = self.x
        bY = self.y
        for i in range(len(self.buttons)):
            self.buttons[i].draw(bX, bY, self.scene)
            if self.direction == 'vertical':
                bY += self.spacing
            if self.direction == 'horizontal':
                bX += self.spacing