from .component import Component

class BattleComponent(Component):

    def __init__(self):
        self.key = 'battle'
        self.hitboxes = {}
        self.hurtboxes = {}

    # hitboxes

    def addHitbox(self, state, hitbox):
        self.hitboxes[state] = hitbox
    
    def getHitbox(self, state):
        if state not in self.hitboxes.keys():
            return None
        return self.hitboxes[state]

    # hurtboxes

    def addHurtbox(self, state, hurtbox):
        self.hurtboxes[state] = hurtbox
    
    def getHurtbox(self, state):
        if state not in self.hurtboxes.keys():
            return None
        return self.hurtboxes[state]
    