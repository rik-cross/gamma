class EntityFactory:
    def __init__(self):
        self.entities = {}
    def addEntity(self, key, entityFunc):
        self.entities[key] = entityFunc
    def create(self, key, x, y):
        return self.entities[key](x,y)