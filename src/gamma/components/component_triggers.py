from ..gamma import inputManager

class TriggersComponent:

    def __init__(self, trigger=None):
        self.key = 'triggers'
        # a list of Interaction objects
        self.triggerList = []
        # add trigger, if one specified
        if trigger is not None:
            self.addTrigger(trigger)
    
    def addTrigger(self, trigger):
        self.triggerList.append(trigger)

class Trigger:

    def __init__(self, boundingBox=None, buttonPress=None):
        self.boundingBox = boundingBox
        # a string representation of a PlayerInput
        # e.g. 'up' or 'b1'
        self.buttonPress = buttonPress
        # to keep track of which entities the trigger is colliding with
        self.last = []
        self.current = []

    # checks whether a button press is required to activate
    # and returns True if either a button press isn't required
    # or the corresponding button has been pressed
    def checkPress(self, entity):
        # if no button press required
        if self.buttonPress is None:
            return True
        # if no input component
        if not entity.hasComponent('input'):
            return True
        # if corresponding button is pressed
        i = entity.getComponent('input')
        b = getattr(i, self.buttonPress)
        if b is not None and inputManager.isDown(b):
            return True
        return False

    def onCollide(self, entity, otherEntity):
        pass

    def onCollisionEnter(self, entity, otherEntity):
        pass

    def onCollisionExit(self, entity, otherEntity):
        pass
