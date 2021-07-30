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

    def update(self):

        # find out whether any input linked to the button is pressed
        down= False
        if self.controlledBy is not None:
            for c in self.controlledBy:

                if inputManager.isDown(c):
                    down = True
                    break
        
        # display the button as pressed or not
        if down:
            self.currentImageGroup = self.pressedImageGroup
            self.defaultImageGroup.reset()
        else:
            self.currentImageGroup = self.defaultImageGroup
            self.pressedImageGroup.reset()
                
        # execute the button (once) if pressed
        for c in self.controlledBy:
            if inputManager.isDown(c):
                if self.actionListener is not None:
                    self.actionListener.execute()
        
        # update the button's current imageGroup
        self.currentImageGroup.update()

    def draw(self, screen):
        # draw button image
        self.currentImageGroup.draw(screen, self.x, self.y)
        # draw button text
        if self.text is not None:
            textX = self.x + self.currentImageGroup.imageList[self.currentImageGroup.imageIndex].get_rect().w + 10
            textY = self.y
            drawText(screen, self.text, textX, textY, fontTag=self.font)