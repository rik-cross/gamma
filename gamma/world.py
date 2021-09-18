import os
import pickle

class World:

    def __init__(self,
        
        map=None,
        entities=None,
        velocityForces = None,
        accelerationForces = None
    
    ):

        # store map
        self.map = map

        # create world entity list
        if entities is None:
            self.entities = []
        else:
            self.entities = entities
        
        # create world forces dictionary
        if velocityForces is None:
            velocityForces = {}
        if accelerationForces is None:
            accelerationForces = {}
        self.forces = {
            'velocity' : velocityForces,
            'acceleration' : accelerationForces
        }

    # world methods

    def addVelocityForce(self, name, force):
        self.forces['velocity'][name] = force

    def addAccelerationForce(self, name, force):
        self.forces['acceleration'][name] = force
    
    def removeForce(self, name):
        if name in self.forces['velocity']:
            del self.forces['velocity'][name]
        if name in self.forces['acceleration']:
            del self.forces['acceleration'][name]

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
    
    def loadMap(self, filename):
        filename = os.path.abspath(filename)
        map =  pickle.load( open( filename, "rb" ) )
        return map

    def saveMap(self, map, filename):
        filename = os.path.abspath(filename)
        pickle.dump( map, open( filename, "wb" ) )