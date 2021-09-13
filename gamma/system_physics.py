from .system import *

class PhysicsSystem(System):

    def init(self):
        self.key = 'physics'

    def setRequirements(self):
        self.requiredComponents = ['position']
    
    def updateEntity(self, entity, scene):
        pass

        #
        # apply world forces
        #

        # velocity

        # acceleration

        #
        # apply entity-specific forces
        #

        # velocity

        # acceleration

        #
        # vertical collision detection
        #

        

        #
        # horizontal collision detection
        #



