from gamma.component import Component
import gamma
from .ui_text import *
from .colours import *
from .colours import *
from .ui_text2 import Text

class TextComponent(Component):

    def __init__(self, text,
        colour = WHITE,
        # minimum text character width
        width = 20,
        # spacing between rows of text
        spacing = 15,
        # display above the entity, or at bottom of scene
        # (not yet implemented)
        overhead = True,
        # how long to display the text
        # options are 'always', 'timed', or 'press'
        lifetime = 'always',
        # how the text appears
        # options are 'appear', 'fade' or 'tick'
        type = 'appear',
        # display a new character every [x] frames
        tick_delay = 5,
        # sound to play when advancing tick animation
        tick_sound = None,
        # display time before fading out (if lifetime='fade')
        final_display_time = 300,
        # inputs that can control the text (if lifetime='press')
        input_list = None
        ):

        self.key = 'text'

        # store component attributes
        
        self.text = text
        self.colour = colour
        self.width = width
        self.spacing = spacing
        self.overhead = overhead
        self.lifetime = lifetime
        self.tick_delay = tick_delay
        self.tick_sound = tick_sound
        self.final_display_time = final_display_time
        self.input_list = input_list
        self.setType(type)

        # attributes to store current state

        # timer used to tick the text forward
        self.delayTimer = self.tick_delay
        # stores the text, divided into rows
        self.textList = []
        # lets the TextSystem know when to delete the component
        self.destroy = False
        # keeps track of fade direction (in or out)
        self.enterOrExit = 'enter'

        # split the text into multiple rows,
        # using self.width as a minimum characher width

        row = ''
        for char in self.text:
            row = row + char
            if len(row) >= self.width and char == ' ':
                self.textList.append(row[:-1])
                row = ''
        if len(row) > 0:
            self.textList.append(row)

    def startExit(self):
        self.enterOrExit = 'exit'

    def setType(self, type):
        # types are 'appear', 'tick' or 'fade'
        self.type = type
        if self.type == 'appear':
            self.finished = True
            self.index = self.width
            self.row = len(self.textList)
            self.fadeAmount = 255
        if self.type == 'tick':
            self.finished = False
            self.index = 0
            self.row = 0
            self.fadeAmount = 255
        if self.type == 'fade':
            self.fadeAmount = 0
            self.finished = False
            self.index = self.width
            self.row = len(self.textList)

    def setLifetime(self, lifetime):
        self.lifetime = lifetime

    def update(self):

        if self.type == 'appear':
            pass

        if self.type == 'tick' and self.enterOrExit == 'enter':
            if not self.finished:
                self.delayTimer -= 1
                if self.delayTimer <= 0:
                    self.delayTimer = self.tick_delay
                    self.index += 1
                    if self.tick_sound:
                        gamma.soundManager.playSound(self.tick_sound, gamma.soundManager.soundVolume / 2)
                    if self.index >= len(self.textList[self.row]):
                        self.index = 0
                        self.row += 1
                        if self.row >= len(self.textList):
                            self.finished = True

        if self.type == 'fade' and self.enterOrExit == 'enter':
            self.fadeAmount = min(self.fadeAmount+4, 255)
            if self.fadeAmount == 255:
                self.finished = True

        if self.finished and self.enterOrExit == 'enter':

            if self.lifetime == 'always':
                pass

            if self.lifetime == 'timed':
                self.final_display_time -= 1
                if self.final_display_time <= 0:
                    self.enterOrExit = 'exit'

        # can press regardless of progress
        if self.lifetime == 'press':
            if self.input_list is not None:
                for input in self.input_list:
                    if gamma.inputManager.isPressed(input):
                        self.enterOrExit = 'exit'
                        
        if self.enterOrExit == 'exit':

            self.fadeAmount = max(self.fadeAmount - 4, 0)
            if self.fadeAmount == 0:
                self.destroy = True

    def draw(self, scene, x, y):      

        rows = self.spacing * len(self.textList)

        for i,l in enumerate(self.textList):

            if i == self.row:
                scene.renderer.add(Text(
                    l[0:self.index],
                    x,
                    y-10-rows+(i*self.spacing),
                    colour=self.colour,
                    alpha=self.fadeAmount
                ))

            elif i < self.row:
                scene.renderer.add(Text(
                    l,
                    x,
                    y-10-rows+(i*self.spacing),
                    colour=self.colour,
                    alpha=self.fadeAmount
                ))