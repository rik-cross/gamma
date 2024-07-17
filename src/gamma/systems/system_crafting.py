from ..core.system import *

class CraftingSystem(System):

    def init(self):
        pass

    def setRequirements(self):
        from ..components.component_crafting import CraftingComponent
        from ..components.component_inventory import InventoryComponent
        self.requiredComponents = [CraftingComponent, InventoryComponent]

    def updateEntity(self, entity, scene):
        from ..components.component_crafting import CraftingComponent
        inv = entity.getComponent(CraftingComponent)
        inv.update()
        
    def drawEntity(self, entity, scene):
        from ..components.component_crafting import CraftingComponent
        entity.getComponent(CraftingComponent).draw(scene)