from .system import *
from .colours import *

class InputSystem(System):

    def init(self):
        self.key = 'input'

    def setRequirements(self):
        self.requiredComponents = ['input']
    
    def updateEntity(self, entity, scene):

        # don't allow input during a cutscene
        if scene.cutscene is not None:
            return

        # run the stored input context
        if entity.getComponent('input').inputContext is not None:
            entity.getComponent('input').inputContext(entity)
        
