from .system import *
from .colours import *

class TraumaSystem(System):

    def init(self):
        self.key = 'trauma'

    def setRequirements(self):
        self.requiredComponents = ['trauma']

    def updateEntity(self, entity, scene):
        # update the entity trauma level each frame
        tc = entity.getComponent('trauma')
        tc.traumaLevel -= tc.traumaDecrement
