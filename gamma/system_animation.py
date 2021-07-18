import pygame
from .system import *
from .colours import *

class AnimationSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['imagegroups']
        self.requiredTags = []

    def updateEntity(self, entity, scene):
        ig = entity.getComponent('imagegroups')
        if entity.state in entity.getComponent('imagegroups').animationList.keys():
            ig.animationList[entity.state].update()