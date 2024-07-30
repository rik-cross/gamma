class System():
    
    def __init__(self):

        self._requiredComponents = []
        self._requiredTags = []
        self.key = None
        self.init()

    # allow systems to initialise themselves
    def init(self):
         pass

    # system will only act on entities with the required set of components
    # (call method without parameters to reset)
    def setRequiredComponents(self, requiredComponent, *moreRequiredComponents):
        self._requiredComponents = [requiredComponent] + list(moreRequiredComponents)

    # system will only act on entities with the required set of tags
    # (call method without parameters to reset)
    def setRequiredTags(self, requredTag, *moreRequiredTags):
        self._requiredTags = [requredTag] + list(moreRequiredTags)

    # checks that a system is only processing the entities that
    # meet the requirements of the system
    def _checkRequirements(self, entity):
        from ..components.component_tags import TagsComponent

        if len(self._requiredComponents) == 0 and len(self._requiredTags) == 0:
            return True

        if len(self._requiredTags) == 0:
            return entity.hasComponent(*self._requiredComponents)

        if len(self._requiredComponents) == 0:
            return entity.getComponent(TagsComponent).has(*self._requiredTags)
        
        return entity.hasComponent(*self._requiredComponents) and entity.getComponent(TagsComponent).has(*self._requiredTags)

    # runs update() and updateEntity() method on all
    # systems that meet the system requirements
    def _update(self, scene):
        
        from ..components.component_tags import TagsComponent

        self.update(scene)
        for entity in scene.entities:
            if self._checkRequirements(entity):
                self.updateEntity(entity, scene)

    # runs once per frame
    def update(self, scene):
        pass

    # processes each entity in a given scene
    def updateEntity(self, entity, scene):
        pass

    # runs draw() and drawEntity() method on all
    # systems that meet the system requirements
    def _draw(self, scene):
        
        for entity in scene.entities:
            if self._checkRequirements(entity):
                self.drawEntity(entity, scene)
    
    # processes each entity in a given scene
    def drawEntity(self, entity, scene):
        pass
