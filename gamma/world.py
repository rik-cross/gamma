import os
import pickle

class World:

    def __init__(self):
        self.entities = []
        self.map = None

    # entity methods

    def addEntity(self, entity):
        self.entities.append(entity)
    
    def deleteEntity(self, entity):
        self.entities.remove(entity)

    def getEntitiesByTag(self, tag, *otherTags):
        entityList = []
        for e in self.entities:
            if e.getComponent('tags').has(tag, *otherTags):
                entityList.append(e)
        return entityList

    def getEntityByID(self, entityID):
        for e in self.entities:
            if e.ID == entityID:
                return e
        return None
    
    def getEntitiesWithComponent(self, *componentKeys):
        entityList = []
        for e in self.entities:
            if e.hasComponent(*componentKeys):
                entityList.append(e)
        return entityList
    
    def clear(self):
        self.entities = []
        self.map = None
    
    # map methods

    def setMap(self, map):
        self.map = map
    
    def loadMap(self, filename, mapImages=[]):
        filename = os.path.abspath(filename)
        map =  pickle.load( open( filename, "rb" ) )
        for img in mapImages:
            map.mapImages.append(img)
        return map

    def saveMap(self, map, filename):
        filename = os.path.abspath(filename)
        pickle.dump( map, open( filename, "wb" ) )