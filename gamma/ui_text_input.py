from gamma.rectangle import Rectangle
from .utils_draw import drawBox
from .text import Text
from .gamma import inputManager, entityManager
from .colours import *
from .keyboard_layouts import *
from .renderable import Renderable
import pygame

class UITextInput(Renderable):

    def __init__(self,

        # optional parameters
        x = 0, y = 0, 
        keyboard = keyboard_layouts['en'],
        text = None,
        hAlign = 'left', vAlign = 'top',
        controllingEntity = None,
        keySize = 50,
        textEntryBoxSize = 80,
        show = True,
        foregroundColour = WHITE,
        backgroundColour = DARK_GREY,
        selectedForegroundColour = BLACK,
        selectedBackgroundColour = WHITE,
        padding = 2
    
    ):

        # initialise renderable element
        super().__init__(x, y, hAlign, vAlign, None, 255)

        self.keyboard = keyboard

        # initialise text
        if text is None:
            self.text = ''
        else:
            self.text = text
    
        # set the controlling entity and get the input component
        self.controllingEntity = controllingEntity
        if self.controllingEntity is not None:
            self.controllingInputComponent = self.controllingEntity.getComponent('input')
        else:
            self.controllingInputComponent = None

        # store other optional parameters
        self.keySize = keySize
        self.textEntryBoxSize = textEntryBoxSize
        self.show = show
        self.foregroundColour = foregroundColour
        self.backgroundColour = backgroundColour
        self.selectedForegroundColour = selectedForegroundColour
        self.selectedBackgroundColour = selectedBackgroundColour
        self.padding = padding
        
        # calculate keyboard width
        self._w = max(map(len, self.keyboard)) * self.keySize
        # calculate keyboard height
        self._h = (len(self.keyboard) * self.keySize) + self.textEntryBoxSize

        # selected key coordinates
        self.cursorX = 0
        self.cursorY = 0

        self._createSurface()

        # displayed text
        self.displayedText = Text(self.text, self.rect.x+10, self.rect.y + self.keySize*len(self.keyboard) + (self.textEntryBoxSize)/2, vAlign='middle')

    def _createSurface(self):
        self.rect = pygame.Rect(self._x, self._y, self._w, self._h)
        self._align()

    def update(self):
        
        if self.controllingInputComponent is None:
            return

        # select key
        if inputManager.isPressed(self.controllingInputComponent.b1):
            # get key
            key = self.keyboard[self.cursorY][self.cursorX]
            # delete
            if key == delete_symbol:
                self.text = self.text[:-1]
            # other keys
            else:
                self.text = self.text + key
            self.displayedText.text = self.text

        # cursor movement
        if inputManager.isPressed(self.controllingInputComponent.up):
            if len(self.keyboard[self.cursorY-1]) > self.cursorX:
                self.cursorY = max(0, self.cursorY - 1)
        if inputManager.isPressed(self.controllingInputComponent.down):
            if len(self.keyboard)-1 > self.cursorY:
                if len(self.keyboard[self.cursorY+1]) > self.cursorX:
                    self.cursorY = min(len(self.keyboard)-1, self.cursorY + 1)
        if inputManager.isPressed(self.controllingInputComponent.left):
            self.cursorX = max(0, self.cursorX - 1)
        if inputManager.isPressed(self.controllingInputComponent.right):
            self.cursorX = min(len(self.keyboard[self.cursorY])-1, self.cursorX + 1)
        
    def draw(self, surface):

        # draw every key on the keyboard
        for c in range(len(self.keyboard)):
            for r in range(len(self.keyboard[c])):
                
                # black border
                Rectangle(self.rect.x+r*self.keySize, self.rect.y+c*self.keySize, self.keySize, self.keySize, colour=BLACK).draw(surface)
                
                # choose colours
                if r == self.cursorX and c == self.cursorY:
                    bg = self.selectedBackgroundColour
                    fg = self.selectedForegroundColour
                else:
                    bg = self.backgroundColour
                    fg = self.foregroundColour

                # key background
                Rectangle(self.rect.x+r*self.keySize+self.padding, self.rect.y+c*self.keySize+self.padding, self.keySize-(self.padding*2), self.keySize-(self.padding*2), colour=bg).draw(surface)
                # key name
                Text(self.keyboard[c][r],self.rect.x+r*self.keySize+(self.keySize/2)+self.padding, self.rect.y+c*self.keySize+(self.keySize/2)+self.padding, hAlign='center', vAlign='middle', colour=fg).draw(surface)
                 
        # text output box and text
        Rectangle(self.rect.x, self.rect.y + self.keySize*len(self.keyboard), self._w, self.textEntryBoxSize, colour=BLACK).draw(surface)
        self.displayedText.draw(surface)
        # cursor
        Text('_', self.displayedText.x + self.displayedText.rect.w, self.displayedText.y, vAlign='middle').draw(surface)

    #  dimension properties

    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, value):
        self._w = value
        self._createSurface()

    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, value):
        self._h = value
        self._createSurface()