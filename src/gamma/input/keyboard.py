import pygame

class Keyboard:

    def __init__(self):
        self.currentKeyStates = None
        self.previousKeyStates = None
        self.durations = None
    
    def processInput(self):
        self.previousKeyStates = self.currentKeyStates
        self.currentKeyStates = pygame.key.get_pressed()
        # long presses
        newDurations = []
        for i in range(len(self.currentKeyStates)):
            if self.currentKeyStates[i] and self.previousKeyStates[i]:
                newDurations.append(self.durations[i]+1)
            else:
                newDurations.append(0)
        self.durations = newDurations

    def isKeyDown(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == True
    
    def isKeyPressed(self, keyCode, long=False):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        if not long:
            return self.currentKeyStates[keyCode] == True and self.previousKeyStates[keyCode] == False
        else:
            return self.durations[keyCode] == 40

    def isKeyReleased(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == False and self.previousKeyStates[keyCode] == True