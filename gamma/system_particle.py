from .system import *

class ParticleSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['emitter']

    def updateEntity(self, entity, scene):
        emt = entity.getComponent('emitter')
        pos = entity.getComponent('position')
        emt.update(pos.rect.x, pos.rect.y)
        if emt.destroy:
            entity.removeComponent('emitter')
            #if entity.getComponent('tags').has('particle'):
            #    scene.world.deleteEntity(entity)
    
    def drawEntity(self, entity, scene):
        entity.getComponent('emitter').draw(scene)