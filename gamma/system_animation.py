from .system import *
from .colours import *

class AnimationSystem(System):

    def init(self):
        self.key = 'animation'

    def setRequirements(self):
        self.requiredComponents = ['imagegroups', 'position']
        self.requiredTags = []
    
    def updateEntity(self, entity, scene):

        ig = entity.getComponent('imagegroups')

        # check that imagegroups state matches global entity state
        # (making sure to reset the 'old' imagegroup before updating)
        if ig.current != entity.state:
            i = ig.getCurrentImageGroup()
            if i is not None:
                i.reset()
            ig.current = entity.state

        # update if an image group exists and is 'playing'
        if ig.current is not None and ig.current in ig.animationList.keys():
            if ig.playing:
                ig.animationList[ig.current].update()
