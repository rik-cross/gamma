import pygame
from .system import *
from .colours import *
import random

class InputSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['input']
    
    def updateEntity(self, entity, scene):
        if entity.getComponent('input').inputFunc is not None:
            entity.getComponent('input').inputFunc(entity)
        
