from .system import *

class TextSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['text']
    
    def updateEntity(self, entity, scene):

        txt = entity.getComponent('text')
        txt.update()

        if txt.destroy:
            entity.removeComponent('text')
    
    def drawEntity(self, entity, scene):

        txt = entity.getComponent('text')
        pos = entity.getComponent('position')
        txt.draw(scene, pos.rect.x, pos.rect.y)

        