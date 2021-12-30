import gamma

class CoinTrigger(gamma.Trigger):

    def onCollisionEnter(self, entity, otherEntity):
        
        if otherEntity.getComponent('tags').has('player'):
            gamma.soundManager.playSound('coin')
            otherEntity.getComponent('score').score += 1
            entity.destroy()