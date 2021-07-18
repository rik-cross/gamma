from .system import *
#from .engine import world

class ParticleSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['emitter']

    def updateEntity(self, entity, scene):
        emt = entity.getComponent('emitter')
        pos = entity.getComponent('position')
        emt.update(pos.rect.x, pos.rect.y)
        if emt.destroy:
            entity.removeComponent('emitter')
            #if len(entity.components) == 4 and entity.hasComponent('emitter', 'position', 'transform', 'tags'):
            #    world.deleteEntity(entity)