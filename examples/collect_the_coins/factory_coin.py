import gamma
from trigger_coin import CoinTrigger
from assets import textureCoin0, textureCoin1, textureCoin2, textureCoin3, textureCoin4, textureCoin5

# function to create new coins, at the given coordinates
def newCoin(x, y):

    # create a coin entity
    coin = gamma.Entity(

        # tag the entity as 'coin'
        gamma.TagsComponent('coin'),

        # coin position is centered on the provided coordinates
        gamma.PositionComponent(x, y, 23, 23, xAnchor='center', yAnchor='middle'),
        
        # create a new coin animation (an image group consisting of 6 frames)
        gamma.SpritesComponent('default', gamma.Sprite(
            # animation contains 6 frames
            textureCoin0, textureCoin1, textureCoin2, textureCoin3, textureCoin4, textureCoin5,
            # delay between animation frames (i.e. animation speed)
            delay=6
        )),
        
        # add a trigger, for when the coin collides with the player
        gamma.TriggersComponent(CoinTrigger(boundingBox=gamma.PositionComponent(0, 0, 23, 23)))
    
    )

    # return the created coin entity
    return coin