import pygame
from .component_transform import TransformComponent
from .component_tags import TagsComponent
from .component_imagegroups import ImageGroups
from .component_intention import Intention

def resetEntity(entity):
    pass

class Entity:
    
    # class-level ID, used to create new entities
    ID = 0

    def __init__(self, *componentList):

        # set and increment the entity id
        self.ID = Entity.ID
        Entity.ID += 1

        # create component dictionary
        # format = {componentKey : component}
        self.components = {}

        # add entity default components
        self.addComponent(ImageGroups())
        self.addComponent(TransformComponent())
        self.addComponent(TagsComponent())
        self.addComponent(Intention())

        # populate component dictionary from passed componenets
        # (this will overwrite existing default components)
        for component in componentList:
            self.addComponent(component)

        self.state = 'idle'         # TODO - remove
        self.direction = 'right'    # TODO - remove?
        self.on_ground = False      # TODO - remove?
        self.reset = resetEntity
        self.trauma = 0
        self.transform = TransformComponent()
        self.tags = TagsComponent()
        self.owner = self
    
    # removes all components from the entity
    def clear(self):
        self.components = {}
    
    # used to reset an entity to an initial state
    def reset(self):
        self.reset()

    def hasComponent(self, componentKey, *otherComponentKeys):
        for c in [componentKey] + list(otherComponentKeys):
            if c not in self.components.keys():
                return False
        return True
    
    def getComponent(self, componentKey):
        if componentKey not in self.components.keys():
            return None
        return self.components[componentKey]

    def addComponent(self, component):
        if component.key is not None:
            self.components[component.key] = component
    
    def removeComponent(self, componentKey):
        if componentKey in self.components.keys():
            self.components.pop(componentKey)