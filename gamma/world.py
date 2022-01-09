import os
import pickle

# functions to sort by x, y, or z position

def sortByX(e):
    pos = e.getComponent('position')
    if pos is None:
        return 1
    return pos.x

def sortByY(e):
    pos = e.getComponent('position')
    if pos is None:    
        return 1
    return pos.y

def sortByZ(e):
    #return e.z
    pos = e.getComponent('position')
    if pos is None:    
        return 1
    return pos.z

class World:

    def __init__(self,
        
        map=None,
        entities=None,
        velocityForces = None,
        accelerationForces = None
    
    ):

        # key to sort
        self.orderKey = sortByZ
        self.orderWhen = 'added' # 'always', 'added' or 'never'

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

        # entities to delete
        self.delete = []

        # a flag to mark entities for reordering
        self.reorderEntities = False

    # world methods

    def _update(self):

        # update entity timed actions
        for e in self.entities:
            for action in e.actions:
                action[0] = max(0, action[0] - 1)
                if action[0] == 0:
                    action[1]()
                    e.actions.remove(action)
        
        # reorder world entities if required
        if self.orderWhen == 'always' or (self.orderWhen == 'added' and self.reorderEntities):
        #if self.reorderEntities:
            self.entities.sort(key = self.orderKey)
            if self.reorderEntities:
                self.reorderEntities = False

        # delete marked entities
        for e in self.entities:
            if e.delete:
                self.entities.remove(e)

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
        self.reorderEntities = True
    
    def deleteEntity(self, entity):
        self.entities.remove(entity)
    
    def deleteEntityByID(self, ID):
        for e in self.entities:
            if e.ID == ID:
                self.deleteEntity(e)

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