class System():
    
    def __init__(self):

        self.requiredComponents = []
        self.requiredTags = []
        self.setRequirements()
        self.key = None
        self.init()

    # allow systems to initialise themselves
    def init(self):
         pass

    # all systems have a set of requirements, and only act on
    # entities with the required set of tags and components
    def setRequirements(self):
        pass

    # checks that a system is only processing the entities that
    # meet the requirements of the system
    def _checkRequirements(self, entity):
        from ..components.component_tags import TagsComponent
        if len(self.requiredComponents) == 0 and len(self.requiredTags) == 0:
            return True
        return entity.hasComponent(*self.requiredComponents) and entity.getComponent(TagsComponent).has(*self.requiredTags)

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
