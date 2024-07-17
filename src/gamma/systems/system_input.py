from ..core.system import *
from ..core.colours import *

class InputSystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_input import InputComponent
        self.requiredComponents = [InputComponent]
    
    def updateEntity(self, entity, scene):

        from ..components.component_input import InputComponent

        # don't allow input during a cutscene
        if scene.cutscene is not None:
            return

        # run the stored input context
        if entity.getComponent(InputComponent).inputContext is not None:
            entity.getComponent(InputComponent).inputContext(entity)
        
