from ..core.system import *

class CraftingSystem(System):

    def init(self):
        from ..components.component_crafting import CraftingComponent
        from ..components.component_inventory import InventoryComponent
        self.setRequiredComponents(CraftingComponent, InventoryComponent)

    def updateEntity(self, entity, scene):
        from ..components.component_crafting import CraftingComponent
        inv = entity.getComponent(CraftingComponent)
        inv.update()
        
    def drawEntity(self, entity, scene):
        from ..components.component_crafting import CraftingComponent
        entity.getComponent(CraftingComponent).draw(scene)