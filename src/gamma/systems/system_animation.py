from ..core.system import *
from ..core.colours import *

class AnimationSystem(System):

    def init(self):
        from ..components.component_sprites import SpritesComponent
        from ..components.component_position import PositionComponent
        self.setRequiredComponents(SpritesComponent, PositionComponent)
    
    def updateEntity(self, entity, scene):
        from ..components.component_sprites import SpritesComponent
        ig = entity.getComponent(SpritesComponent)

        #from ..components.component_tags import TagsComponent
        #tc = entity.getComponent(TagsComponent)
        #print(tc.tags, scene.frame)

        # check that Sprites state matches global entity state
        # (making sure to reset the 'old' Sprite before updating)
        if ig.current != entity.state:
            i = ig.getCurrentSprite()
            if i is not None:
                i.reset()
            ig.current = entity.state

        # update if a sprite exists and is 'playing'
        if ig.current is not None and ig.current in ig.spriteList.keys():
            if ig.playing:
                ig.spriteList[ig.current].update()
