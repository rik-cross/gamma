from ..core.system import *

class ParticleSystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_particle_emitter import ParticleEmitterComponent
        self.requiredComponents = [ParticleEmitterComponent]

    def updateEntity(self, entity, scene):

        from ..components.component_position import PositionComponent
        from ..components.component_particle_emitter import ParticleEmitterComponent
        from ..components.component_tags import TagsComponent

        emt = entity.getComponent(ParticleEmitterComponent)
        pos = entity.getComponent(PositionComponent)
        
        # update the particles
        emt.update(pos.rect.x, pos.rect.y)

        # destroy if it has finished emitting particles
        if emt.destroy:
            entity.removeComponent(ParticleEmitterComponent)

            # delete the entity if it serves only as a particle emitter
            if entity.getComponent(TagsComponent).has('particle'):
                scene.deleteEntity(entity)
    
    def drawEntity(self, entity, scene):
        from ..components.component_particle_emitter import ParticleEmitterComponent
        entity.getComponent(ParticleEmitterComponent).draw(scene)