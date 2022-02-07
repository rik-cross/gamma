from .system import *

class ParticleSystem(System):

    def init(self):
        self.key = 'particle'

    def setRequirements(self):
        self.requiredComponents = ['emitter']

    def updateEntity(self, entity, scene):

        emt = entity.getComponent('emitter')
        pos = entity.getComponent('position')
        
        # update the particles
        emt.update(pos.rect.x, pos.rect.y)

        # destroy if it has finished emitting particles
        if emt.destroy:
            entity.removeComponent('emitter')

            # delete the entity if it serves only as a particle emitter
            if entity.getComponent('tags').has('particle'):
                scene.deleteEntity(entity)
    
    def drawEntity(self, entity, scene):
        entity.getComponent('emitter').draw(scene)