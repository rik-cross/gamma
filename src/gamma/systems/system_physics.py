from ..core.system import *

class PhysicsSystem(System):

    def init(self):
        from ..components.component_position import PositionComponent
        self.setRequiredComponents(PositionComponent)
    
    def updateEntity(self, entity, scene):

        from ..components.component_position import PositionComponent
        from ..components.component_motion import MotionComponent

        pass

        #
        # apply scene forces
        #

        # velocity

        # acceleration

        #
        # apply entity-specific forces
        #

        # velocity

        if entity.hasComponent(MotionComponent):
            m = entity.getComponent(MotionComponent)
            if m.velocity is not None:
                p = entity.getComponent(PositionComponent)
                p.x += m.velocity.x
                p.y += m.velocity.y

        # acceleration

        #
        # vertical collision detection
        #

        

        #
        # horizontal collision detection
        #



