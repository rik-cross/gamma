from .system import *
from .colours import *

class TraumaSystem(System):

    def updateEntity(self, entity, scene):    
        entity.trauma =  max(0, entity.trauma - 0.01 )