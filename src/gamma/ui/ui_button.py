from ..gamma import inputManager
from ..renderables.text import Text
from ..renderables.image import Image
from .ui_text import drawText

class UIButton:

    def __init__(self, x, y, defaultSprite, pressedSprite, controlledBy=None, actionListener=None, text=None, font='munro24'):

        self.x = x
        self.y = y

        self.defaultSprite = defaultSprite
        self.pressedSprite = pressedSprite
        self.currentSprite = self.defaultSprite

        if self.defaultSprite is not None:
            self.defaultSprite.loop = False
        if self.pressedSprite is not None:
            self.pressedSprite.loop = False

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
        if self.defaultSprite is not None and self.pressedSprite is not None:
            if self.downCurrent:
                self.currentSprite = self.pressedSprite
            else:
                self.currentSprite = self.defaultSprite

        # reset Sprite on state change
        if self.downCurrent is not self.downPrevious:
            if self.pressedSprite is not None:
                self.pressedSprite.reset()

        # execute the button (once) if pressed
        for c in self.controlledBy:
            if inputManager.isPressed(c):
                if self.actionListener is not None:
                    if self.active:
                        self.actionListener.execute()
        
        # update the button's current Sprite
        if self.currentSprite is not None:
            self.currentSprite.update()

    def draw(self, surface):

        # calculate alpha
        alpha = 255
        if not self.active:
            alpha = 100

        # draw button image
        if self.currentSprite is not None:

            image = self.currentSprite.textureList[self.currentSprite.textureIndex]

            if image is not None:
                image = image.copy()
                Image(image, self.x, self.y, alpha=alpha).draw(surface)
                
                # draw button text
                if self.text is not None:
                    textX = self.x + self.currentSprite.textureList[self.currentSprite.textureIndex].get_rect().w + 10
                    textY = self.y
                    Text(self.text, textX, textY, alpha=alpha).draw(surface)
