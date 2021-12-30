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

        if entity.hasComponent('motion'):
            m = entity.getComponent('motion')
            if m.velocity is not None:
                p = entity.getComponent('position')
                p.x += m.velocity.x
                p.y += m.velocity.y

        # acceleration

        #
        # vertical collision detection
        #

        

        #
        # horizontal collision detection
        #



