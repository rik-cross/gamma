from .system import *

class CraftingSystem(System):

    def init(self):
        self.key = 'crafting'

    def setRequirements(self):
        self.requiredComponents = ['crafting', 'inventory']

    def updateEntity(self, entity, scene):
        
        inv = entity.getComponent('crafting')
        inv.update()
        
    def drawEntity(self, entity, scene):
        entity.getComponent('crafting').draw(scene)