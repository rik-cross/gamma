from .ui_action_listener import *
from ..renderables.text import Text
from ..core.colours import *

class UITextMenuItem:

    def __init__(self, text, actionListener=None, active=True):

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
        self.inactiveColour = MID_GREY

        self.colour = self.normalColour

        self.width = 100
        self.height = 45
        self.text = text

        self._active = active

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
        
        if not self.active:
            self.colour = self.inactiveColour
        
    def draw(self, x, y, scene):
        # draw the menu item text
        t = Text(self.text, x, y, colour=self.colour, underline=False, hAlign='center')
        t.draw(scene.surface)
        # mark the currently selected item
        if self.colour is not self.normalColour and self.colour is not self.inactiveColour:
            Text('>', x - (t.rect.w//2) - 10, y, colour=self.colour, underline=False, hAlign='right').draw(scene.surface)
    
    # active

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
        self.reset()