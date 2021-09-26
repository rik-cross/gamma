from .gamma import inputManager

class TriggersComponent:

    def __init__(self):
        self.key = 'triggers'
        # a list of Interaction objects
        self.triggerList = []
    
    def addTrigger(self, trigger):
        self.triggerList.append(trigger)

class Trigger:

    def __init__(self, boundingBox=None, buttonPress=None):
        self.boundingBox = boundingBox
        self.buttonPress = buttonPress
        # to keep track of which entities the trigger is colliding with
        self.last = []
        self.current = []

    # checks whether a button press is required to activate
    # and returns True if either a button press isn't required
    # or the corresponding button has been pressed
    def checkPress(self):
        if self.buttonPress is None:
            return True
        if self.buttonPress is not None and inputManager.isDown(self.buttonPress):
            return True
        return False

    def onCollide(self, entity, otherEntity):
        pass

    def onCollisionEnter(self, entity, otherEntity):
        pass

    def onCollisionExit(self, entity, otherEntity):
        pass
