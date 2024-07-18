class Entity:
    
    # class-level ID, used to create new entities
    ID = 0

    def __init__(self, *componentList):

        # set and increment the entity id
        self.ID = Entity.ID
        Entity.ID += 1

        # set initial default state
        self.state = 'default'
        self.prevState = 'default'

        # deletion flag
        self.delete = False

        # create component list
        self.components = []

        self._addDefaultComponents()

        # populate component dictionary from passed componenets
        # (this will overwrite existing default components)
        for component in componentList:
            self.addComponent(component)

        # every entity has an owner, default = self
        self.owner = self

        # timed actions
        self.actions = []
    
    def _update(self):
        self.prevState = self.state

    # add entity default components
    def _addDefaultComponents(self):
        from ..components.component_tags import TagsComponent
        from ..components.component_sprites import SpritesComponent
        self.addComponent(SpritesComponent())
        self.addComponent(TagsComponent())

    # set entity state
    def setState(self, state):
        self.state = state

    # removes all components from the entity
    def clear(self):
        self.components = []
        self._addDefaultComponents()
    
    # used to reset an entity to an initial state
    def reset(self):
        # defer to each component reset() method
        for c in self.components:
            c.reset()
        self.state = 'default'
    
    # delete an entity
    def destroy(self):
        self.delete = True

    # returns true if entity has a component of all included types
    def hasComponent(self, componentType, *moreComponentTypes):
        return set([componentType] + list(moreComponentTypes)).issubset(set([type(c) for c in self.components]))

    # uses the passed type to return a component
    def getComponent(self, componentType):
        for c in self.components:
            if type(c) == componentType:
                return c
        return None

    #adds a component to the entity component list
    def addComponent(self, component, *moreComponents):
        for c in [component] + list(moreComponents):
            if self.hasComponent(type(c)):
                self.removeComponent(type(c))
            self.components.append(c)
    
    # removes the specified component
    def removeComponent(self, componentType, *moreComponentTypes):
        for c in self.components:
            if type(c) in [componentType] + list(moreComponentTypes):
                self.components.remove(c)
    
    # perform an action after a set number of frames
    def after(self, frames, action):
        self.actions.append([frames, action])
    
    # method run when entity is added to a scene
    def onAddedToScene(self):
        pass

     # method run when entity is removed from a scene
    def onRemovedFromScene(self):
        pass
