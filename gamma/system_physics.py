from .system import *

class PhysicsSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['position']
    
    def updateEntity(self, entity, scene):
        pass