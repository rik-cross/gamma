import pygame
from .system import *
from .colours import *

class TraumaSystem(System):

    def _check(self, entity):
        return entity.trauma is not None
    
    def updateEntity(self, entity, scene):    
        entity.trauma =  max(0, entity.trauma - 0.01 )