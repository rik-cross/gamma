class System():
    
    def __init__(self):
        self.requiredComponents = []
        self.requiredTags = []
        # all systems run as part of a scene update() method,
        # but those tagged as 'requiresDraw' instead run as part
        # of the scene draw() method
        self.requiresDraw = False
        self.setRequirements()        

    # all systems have a set of requirements, and only act on
    # entities with the required set of tags and components
    def setRequirements(self):
        pass

    # checks that a system is only processing the entities that
    # meet the requirements of the system
    def _checkRequirements(self, entity):
        if len(self.requiredComponents) == 0:
            return True
        return entity.hasComponent(*self.requiredComponents) and entity.getComponent('tags').has(*self.requiredTags)

    # runs the 'updateEntity() method on all systems that
    # meet the system requirements
    # TODO - name as _update(), as it's internal
    def update(self, scene):
        for entity in scene.world.entities:
            if self._checkRequirements(entity):
                self.updateEntity(entity, scene)

    # this method processes each entity in a given scene
    def updateEntity(self, entity, scene):
        pass
