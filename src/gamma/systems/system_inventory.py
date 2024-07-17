from ..core.system import *

class InventorySystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_inventory import InventoryComponent
        self.requiredComponents = [InventoryComponent]

    def updateEntity(self, entity, scene):
        pass
        
    def drawEntity(self, entity, scene):
        from ..components.component_inventory import InventoryComponent
        entity.getComponent(InventoryComponent).draw(scene)