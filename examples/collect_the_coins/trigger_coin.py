import gamma
from component_score import ScoreComponent

# a trigger attached to a coin
# to allow players to collect them
class CoinTrigger(gamma.Trigger):

    # called whenever an entity with a collider component
    # collides with the trigger area
    def onCollisionEnter(self, entity, otherEntity):
        
        # if the other entity is tagged as a 'player'
        if otherEntity.getComponent(gamma.TagsComponent).has('player'):
            
            # play a sound stored in the sound manager
            gamma.soundManager.playSound('coin')
            
            # add one to the player score, using the 'score' component
            otherEntity.getComponent(ScoreComponent).score += 1
            
            # delete the coin
            entity.destroy()