class TriggersComponent:

    def __init__(self):
        self.key = 'triggers'
        # a list of Interaction objects
        self.triggerList = []
    
    def addTrigger(self, trigger):
        self.triggerList.append(trigger)

class Trigger:

    def __init__(self, boundingBox=None):
        self.boundingBox = boundingBox
        # to keep track of which entities the trigger is colliding with
        self.last = []
        self.current = []

    def onCollide(self, otherEntity):
        pass

    def onCollisionEnter(self, otherEntity):
        pass

    def onCollisionExit(self, otherEntity):
        pass
