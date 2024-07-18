from ..core.system import *

class TextSystem(System):

    def init(self):
        from ..components.component_text import TextComponent
        self.setRequiredComponents(TextComponent)

    def updateEntity(self, entity, scene):

        from ..components.component_text import TextComponent
        from ..components.component_tags import TagsComponent

        txt = entity.getComponent(TextComponent)
        txt.update()

        if txt.destroy:
            entity.removeComponent(TextComponent)

        # delete the entity if it serves only as a particle emitter
        if entity.getComponent(TagsComponent).has('text'):
            scene.deleteEntity(entity)

    def drawEntity(self, entity, scene):

        from ..components.component_text import TextComponent
        from ..components.component_position import PositionComponent

        txt = entity.getComponent(TextComponent)
        pos = entity.getComponent(PositionComponent)

        txt.draw(scene, pos.rect.x, pos.rect.y)