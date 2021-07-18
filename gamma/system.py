class System():

    systems = []

    @classmethod
    def addSystem(cls, system):
        cls.systems.append(system)
    
    def __init__(self):
        self.requiredComponents = []
        self.requiredTags = []
        self.requiresDraw = False
        self.setRequirements()        
        
    def setRequirements(self):
        pass

    def _check(self, entity):
        if len(self.requiredComponents) == 0:
            return False
        return entity.hasComponent(*self.requiredComponents) and entity.getComponent('tags').has(*self.requiredTags)

    def update(self, scene):
        for entity in scene.world.entities:
            if self._check(entity):
                self.updateEntity(entity, scene)

    def updateEntity(self, entity, scene):
        pass

    @classmethod
    def swap(cls, s1, s2):
        cls.systems[s1], cls.systems[s2] = cls.systems[s2], cls.systems[s1]