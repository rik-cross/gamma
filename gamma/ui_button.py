from .ui_action_listener import *
from .ui_text import *
from .colours import *

class ButtonUI:

    def __init__(self, text, actionListener=None):

        self.actionListener = actionListener

        self.activeCurrent = False
        self.activePrevious = False
        
        self.pressedCurrent = False
        self.pressedPrevious = False

        self.activeLength = 35
        self.pressedTimer = 0

        self.execNextFrame = False

        self.normalColour = LIGHT_GREY
        self.activeColour = WHITE
        self.pressedColour = GREEN

        self.colour = self.normalColour

        self.width = 100
        self.height = 45
        self.text = text

    def reset(self):

        self.activeCurrent = False
        self.activePrevious = False
        
        self.pressedCurrent = False
        self.pressedPrevious = False

        self.pressedTimer = 0

        self.execNextFrame = False

        self.colour = self.normalColour

    def update(self, active, pressed):

        self.activePrevious = self.activeCurrent
        self.activeCurrent = active
        activatedThisFrame = self.activeCurrent and not self.activePrevious
        deactivatedThisFrame = self.activePrevious and not self.activeCurrent

        self.pressedPrevious = self.pressedCurrent
        self.pressedCurrent = pressed
        pressedThisFrame = self.pressedCurrent and not self.pressedPrevious
        releasedThisFrame = self.pressedPrevious and not self.pressedCurrent

        if self.execNextFrame:
            self.execNextFrame = False
            if self.actionListener is not None:
                self.actionListener.execute()

        if pressed:
            self.pressedTimer = self.activeLength
        
        if pressedThisFrame:
            self.execNextFrame = True

        if self.pressedTimer > 0:
            self.colour = self.pressedColour
            self.pressedTimer = max(0, self.pressedTimer - 1)
            if self.pressedTimer == 0:
                if pressed:
                    self.colour = self.pressedColour
                elif active:
                    self.colour = self.activeColour
                else:
                    self.colour = self.normalColour

        if activatedThisFrame:
            self.colour = self.activeColour
        
        if deactivatedThisFrame:
            self.colour = self.normalColour
        
    def draw(self, x, y, scene):
        drawText(scene.surface, self.text, x, y, self.colour, hAlign='center', underline=self.colour is not self.normalColour)