from .gamma import inputManager
from .ui_text import drawText

class UIButton:

    def __init__(self, x, y, defaultImageGroup, pressedImageGroup, controlledBy=None, actionListener=None, text=None, font='munro24'):

        self.x = x
        self.y = y

        self.defaultImageGroup = defaultImageGroup
        self.pressedImageGroup = pressedImageGroup
        self.currentImageGroup = self.defaultImageGroup

        self.defaultImageGroup.loop = False
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

        if not self.active:
            return

        self.downPrevious = self.downCurrent

        # find out whether any input linked to the button is pressed
        self.downCurrent = False
        if self.controlledBy is not None:
            for c in self.controlledBy:

                if inputManager.isDown(c):
                    self.downCurrent = True
                    break
        
        # display the button as pressed or not
        if self.downCurrent:
            self.currentImageGroup = self.pressedImageGroup
        else:
            self.currentImageGroup = self.defaultImageGroup

        # reset imageGroup on state change
        if self.downCurrent is not self.downPrevious:
            self.pressedImageGroup.reset()

        # execute the button (once) if pressed
        for c in self.controlledBy:
            if inputManager.isPressed(c):
                if self.actionListener is not None:
                    self.actionListener.execute()
        
        # update the button's current imageGroup
        self.currentImageGroup.update()

    def draw(self, screen):

        alpha = 255
        if not self.active:
            alpha = 100

        # draw button image
        self.currentImageGroup.draw(screen, self.x, self.y, alpha=alpha)
        # draw button text
        if self.text is not None:
            textX = self.x + self.currentImageGroup.imageList[self.currentImageGroup.imageIndex].get_rect().w + 10
            textY = self.y
            drawText(screen, self.text, textX, textY, alpha=alpha, fontTag=self.font)