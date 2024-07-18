from ..core.system import *

class InventorySystem(System):

    def init(self):
        from ..components.component_inventory import InventoryComponent
        self.setRequiredComponents(InventoryComponent)

    def updateEntity(self, entity, scene):
        pass
        
    def drawEntity(self, entity, scene):
        from ..components.component_inventory import InventoryComponent
        entity.getComponent(InventoryComponent).draw(scene)