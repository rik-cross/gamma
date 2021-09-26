from .system import *

class InventorySystem(System):

    def init(self):
        self.key = 'inventory'

    def setRequirements(self):
        self.requiredComponents = ['inventory']

    def updateEntity(self, entity, scene):
        
        inv = entity.getComponent('inventory')
        inv.update()
        
    def drawEntity(self, entity, scene):
        entity.getComponent('inventory').draw(scene)