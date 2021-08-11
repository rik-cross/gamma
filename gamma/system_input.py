from .system import *
from .colours import *

class InputSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['input']
    
    def updateEntity(self, entity, scene):

        if scene.cutscene is not None:
            return

        if entity.getComponent('input').inputFunc is not None:
            entity.getComponent('input').inputFunc(entity)
        
