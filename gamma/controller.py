import pygame

class Controller:
    def __init__(self, number):
        self.number = number
        self.joystick = None
        if number <= pygame.joystick.get_count()-1:
            self.joystick = pygame.joystick.Joystick(number)
            self.joystick.init()
            self.name = self.joystick.get_name()
        self.previousButtons = None
        self.currentButtons = None
        self.previousAxes = None
        self.currentAxes = None
        self.previousHats = None
        self.currentHats = None
    def processInput(self):
        if self.joystick is None:
            return
        self.previousButtons = self.currentButtons
        self.currentButtons = []
        for b in range(self.joystick.get_numbuttons()):
            self.currentButtons.append(self.joystick.get_button(b))
        self.previousAxes = self.currentAxes
        self.currentAxes = []
        for a in range(self.joystick.get_numaxes()):
            self.currentAxes.append(self.joystick.get_axis(a))
        self.previousHats = self.currentHats
        self.currentHats = []
        for h in range(self.joystick.get_numhats()):
            self.currentHats.append(self.joystick.get_hat(h))
    def isButtonDown(self, controllerInput):
        if self.currentButtons is None:
            return False
        if len(self.currentButtons) <= controllerInput.inputNumber:
            return False
        return self.currentButtons[controllerInput.inputNumber] >= controllerInput.threshhold
    def isButtonPressed(self, controllerInput):
        if self.currentButtons is None or self.previousButtons is None:
            return False
        if len(self.currentButtons) <= controllerInput.inputNumber:
            return False
        return self.currentButtons[controllerInput.inputNumber] >= controllerInput.threshhold and self.previousButtons[controllerInput.inputNumber] < controllerInput.threshhold
    def isButtonReleased(self, controllerInput):
        if len(self.currentButtons) <= controllerInput.inputNumber:
            return False
        if self.currentButtons is None or self.previousButtons is None:
            return False
        return self.currentButtons[controllerInput.inputNumber] <= controllerInput.threshhold and self.previousButtons[controllerInput.inputNumber] > controllerInput.threshhold
    
    def isHatDown(self, controllerInput):
        if self.currentHats is None:
            return False
        if len(self.currentHats) <= controllerInput.inputNumber[0]:
            return False
        if controllerInput.threshhold > 0:
            return self.currentHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] >= controllerInput.threshhold
        else:
            return self.currentHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] <= controllerInput.threshhold
    def isHatPressed(self, controllerInput):
        if self.currentHats is None or self.previousHats is None:
            return False
        if len(self.currentHats) <= controllerInput.inputNumber[0]:
            return False
        if controllerInput.threshhold > 0:
            return self.currentHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] >= controllerInput.threshhold and self.previousHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] < controllerInput.threshhold
        else:
            return self.currentHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] <= controllerInput.threshhold and self.previousHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] > controllerInput.threshhold
    def isHatReleased(self, controllerInput):
        if self.currentHats is None or self.previousHats is None:
            return False
        if len(self.currentHats) <= controllerInput.inputNumber[0]:
            return False
        if controllerInput.threshhold > 0:
            return self.currentHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] < controllerInput.threshhold and self.previousHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] >= controllerInput.threshhold
        else:
            return self.currentHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] > controllerInput.threshhold and self.previousHats[controllerInput.inputNumber[0]][controllerInput.inputNumber[1]] <= controllerInput.threshhold

    def isAxisDown(self, controllerInput):
        if self.currentAxes is None:
            return False
        if len(self.currentAxes) <= controllerInput.inputNumber:
            return False
        if controllerInput.threshhold > 0:
            return self.currentAxes[controllerInput.inputNumber] >= controllerInput.threshhold
        else:
            return self.currentAxes[controllerInput.inputNumber] <= controllerInput.threshhold
    def isAxisPressed(self, controllerInput):
        if self.currentAxes is None or self.previousAxes is None:
            return False
        if len(self.currentAxes) <= controllerInput.inputNumber:
            return False
        if controllerInput.threshhold > 0:
            return self.currentAxes[controllerInput.inputNumber] >= controllerInput.threshhold and self.previousAxes[controllerInput.inputNumber] < controllerInput.threshhold
        else:
            return self.currentAxes[controllerInput.inputNumber] <= controllerInput.threshhold and self.previousAxes[controllerInput.inputNumber] > controllerInput.threshhold
    def isAxisReleased(self, controllerInput):
        if self.currentAxes is None or self.previousAxes is None:
            return False
        if len(self.currentAxes) <= controllerInput.inputNumber:
            return False
        if controllerInput.threshhold > 0:
            return self.currentAxes[controllerInput.inputNumber] < controllerInput.threshhold and self.previousAxes[controllerInput.inputNumber] >= controllerInput.threshhold
        else:
            return self.currentAxes[controllerInput.inputNumber] > controllerInput.threshhold and self.previousAxes[controllerInput.inputNumber] <= controllerInput.threshhold
