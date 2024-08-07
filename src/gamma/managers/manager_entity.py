class EntityManager:

    def __init__(self):
        self.entities = []

    def addEntity(self, entity):
        self.entities.append(entity)
    
    def deleteEntity(self, entity):
        self.entities.remove(entity)
    
    def deleteEntityByID(self, ID):
        for e in self.entities:
            if e.ID == ID:
                self.deleteEntity(e)

    def getEntitiesByTag(self, tag, *otherTags):
        from ..components.component_tags import TagsComponent
        entityList = []
        for e in self.entities:
            if e.getComponent(TagsComponent).has(tag, *otherTags):
                entityList.append(e)
        return entityList

    def getEntityByID(self, entityID):
        for e in self.entities:
            if e.ID == entityID:
                return e
        return None
    
    def getEntitiesWithComponent(self, *componentTypes):
        entityList = []
        for e in self.entities:
            if e.hasComponent(*componentTypes):
                entityList.append(e)
        return entityList
    
    def clear(self):
        self.entities = []