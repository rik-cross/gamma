from .system import *
from .colours import *

class AnimationSystem(System):

    def init(self):
        self.key = 'animation'

    def setRequirements(self):
        self.requiredComponents = ['sprites', 'position']
        self.requiredTags = []
    
    def updateEntity(self, entity, scene):

        ig = entity.getComponent('sprites')

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
