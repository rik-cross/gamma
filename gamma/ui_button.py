from .ui_text2 import Text
from .image import Image
from .gamma import inputManager
from .ui_text import drawText

class UIButton:

    def __init__(self, x, y, defaultImageGroup, pressedImageGroup, controlledBy=None, actionListener=None, text=None, font='munro24'):

        self.x = x
        self.y = y

        self.defaultImageGroup = defaultImageGroup
        self.pressedImageGroup = pressedImageGroup
        self.currentImageGroup = self.defaultImageGroup

        if self.defaultImageGroup is not None:
            self.defaultImageGroup.loop = False
        if self.pressedImageGroup is not None:
            self.pressedImageGroup.loop = False

        # a list of entities that can press the button
        self.controlledBy = controlledBy

        # function to call is pressed
        self.actionListener = actionListener

        # button text
        self.text = text
        self.font = font

        self.downCurrent = False
        self.downPrevious = False

        self.active = True

    def update(self):

        self.downPrevious = self.downCurrent

        # find out whether any input linked to the button is pressed
        self.downCurrent = False
        if self.controlledBy is not None:
            for c in self.controlledBy:

                if inputManager.isDown(c):
                    self.downCurrent = True
                    break
        
        # display the button as pressed or not
        if self.defaultImageGroup is not None and self.pressedImageGroup is not None:
            if self.downCurrent:
                self.currentImageGroup = self.pressedImageGroup
            else:
                self.currentImageGroup = self.defaultImageGroup

        # reset imageGroup on state change
        if self.downCurrent is not self.downPrevious:
            if self.pressedImageGroup is not None:
                self.pressedImageGroup.reset()

        # execute the button (once) if pressed
        for c in self.controlledBy:
            if inputManager.isPressed(c):
                if self.actionListener is not None:
                    if self.active:
                        self.actionListener.execute()
        
        # update the button's current imageGroup
        if self.currentImageGroup is not None:
            self.currentImageGroup.update()

    def draw(self, surface):

        # calculate alpha
        alpha = 255
        if not self.active:
            alpha = 100

        # draw button image
        if self.currentImageGroup is not None:

            image = self.currentImageGroup.imageList[self.currentImageGroup.imageIndex]

            if image is not None:
                image = image.copy()
                Image(image, self.x, self.y, alpha=alpha).draw(surface)
                
                # draw button text
                if self.text is not None:
                    textX = self.x + self.currentImageGroup.imageList[self.currentImageGroup.imageIndex].get_rect().w + 10
                    textY = self.y
                    Text(self.text, textX, textY, alpha=alpha).draw(surface)
