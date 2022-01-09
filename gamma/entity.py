from .component_tags import TagsComponent
from .component_imagegroups import ImageGroupsComponent

class Entity:
    
    # class-level ID, used to create new entities
    ID = 0

    def __init__(self, *componentList):

        # set and increment the entity id
        self.ID = Entity.ID
        Entity.ID += 1

        # deletion flag
        self.delete = False

        # create component dictionary
        # format = {componentKey : component}
        self.components = {}

        self._addDefaultComponents()

        # populate component dictionary from passed componenets
        # (this will overwrite existing default components)
        for component in componentList:
            self.addComponent(component)

        # every entity has an owner, default = self
        self.owner = self

        # timed actions
        self.actions = []
    
    # add entity default components
    def _addDefaultComponents(self):
        if not self.hasComponent('imagegroups'):
            self.addComponent(ImageGroupsComponent())
        if not self.hasComponent('tags'):
            self.addComponent(TagsComponent())

    # removes all components from the entity
    def clear(self):
        self.components = {}
        self._addDefaultEntities()
    
    # used to reset an entity to an initial state
    def reset(self):
        # defer to each component reset() method
        for c in self.components.values:
            c.reset()
    
    # delete an entity
    def destroy(self):
        self.delete = True

    # returns true is entity has all passed component keys
    def hasComponent(self, componentKey, *otherComponentKeys):
        for c in [componentKey] + list(otherComponentKeys):
            if c not in self.components.keys():
                return False
        return True
    
    # uses the passed key to return a component
    def getComponent(self, componentKey):
        if componentKey not in self.components.keys():
            return None
        return self.components[componentKey]

    #adds a component to the entity component list
    def addComponent(self, component):
        if component.key is not None:
            self.components[component.key] = component
    
    # removes the specified component
    def removeComponent(self, componentKey):
        if componentKey in self.components.keys():
            self.components.pop(componentKey)
    
    # perform an action after a set number of frames
    def after(self, frames, action):
        self.actions.append([frames, action])