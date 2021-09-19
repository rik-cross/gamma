from .system import *

class TextSystem(System):

    def init(self):
        self.key = 'text'

    def setRequirements(self):
        self.requiredComponents = ['text']

    def updateEntity(self, entity, scene):

        txt = entity.getComponent('text')
        txt.update()

        if txt.destroy:
            entity.removeComponent('text')

        # delete the entity if it serves only as a particle emitter
        if entity.getComponent('tags').has('text'):
            scene.world.deleteEntity(entity)

    def drawEntity(self, entity, scene):

        txt = entity.getComponent('text')
        pos = entity.getComponent('position')

        txt.draw(scene, pos.rect.x, pos.rect.y)