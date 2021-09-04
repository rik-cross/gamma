from .system import *
from .colours import *
#from .image import Image

class AnimationSystem(System):

    def init(self):
        self.key = 'animation'

    def setRequirements(self):
        self.requiredComponents = ['imagegroups', 'position']
        self.requiredTags = []

    def updateEntity(self, entity, scene):
        ig = entity.getComponent('imagegroups')
        if ig.current is not None:
            if ig.playing:
                ig.animationList[ig.current].update()
