from ..gamma import inputManager
from ..core.component import Component

class TriggersComponent(Component):

    def __init__(self, trigger=None):
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
        from ..components.component_input import InputComponent
        # if no button press required
        if self.buttonPress is None:
            return True
        # if no input component
        if not entity.hasComponent(InputComponent):
            return True
        # if corresponding button is pressed
        i = entity.getComponent(InputComponent)
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
