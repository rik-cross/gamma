from ..core.system import *
from ..core.colours import *

class TraumaSystem(System):

    def init(self):
        from ..components.component_trauma import TraumaComponent
        self.setRequiredComponents(TraumaComponent)

    def updateEntity(self, entity, scene):
        from ..components.component_trauma import TraumaComponent
        # update the entity trauma level each frame
        tc = entity.getComponent(TraumaComponent)
        tc.traumaLevel -= tc.traumaDecrement
