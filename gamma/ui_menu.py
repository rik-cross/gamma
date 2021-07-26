from .colours import *
from .gamma import inputManager
from .inputmanager import keys

class Menu:

    def __init__(self, x, y, buttons=None, direction='vertical', spacing=50, entities=[], normalColour=LIGHT_GREY, activeColour=WHITE, pressedColour=GREEN):
        
        self.normalColour = normalColour
        self.activeColour = activeColour
        self.pressedColour = pressedColour

        if buttons is None:
            self.buttons = []
        else:
            self.buttons = buttons
        
        for b in self.buttons:
            self.setButtonColour(b)

        self.activeButtonIndex = 0
        self.x = x
        self.y = y
        self.direction = direction
        self.spacing = spacing

        self.entities = entities

    def addButton(self, button):
        self.buttons.append(button)
        self.setButtonColour(button)
    
    def setButtonColour(self, button):
        button.normalColour = self.normalColour
        button.activeColour = self.activeColour
        button.pressedColour = self.pressedColour

    def reset(self):
        self.activeButtonIndex = 0
        for b in self.buttons:
            b.reset()
        if len(self.buttons) > 0:
            self.buttons[0].update(True, False)

    def update(self):

        for e in self.entities:
            if e.hasComponent('input'):
                if self.direction == 'vertical':
                    if inputManager.isPressed(e.getComponent('input').up):
                        self.activeButtonIndex = max(0, self.activeButtonIndex - 1)
                    if inputManager.isPressed(e.getComponent('input').down):
                        self.activeButtonIndex = min(len(self.buttons)-1, self.activeButtonIndex + 1)
                elif self.direction == 'horizontal':
                    if inputManager.isPressed(e.getComponent('input').left):
                        self.activeButtonIndex = max(0, self.activeButtonIndex - 1)
                    if inputManager.isPressed(e.getComponent('input').right):
                        self.activeButtonIndex = min(len(self.buttons)-1, self.activeButtonIndex + 1)

        # update buttons in the button group
        pressed = False
        for e in self.entities:
            if e.hasComponent('input'):
                if inputManager.isPressed(e.getComponent('input').b1):
                    pressed = True
                    break

        for i in range(len(self.buttons)):
            self.buttons[i].update(self.activeButtonIndex == i, self.activeButtonIndex == i and pressed)

    def draw(self):
        bX = self.x
        bY = self.y
        for i in range(len(self.buttons)):
            self.buttons[i].draw(bX, bY, self.scene)
            if self.direction == 'vertical':
                bY += self.spacing
            if self.direction == 'horizontal':
                bX += self.spacing