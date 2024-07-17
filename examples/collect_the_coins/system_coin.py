import gamma
from random import randint

# system to ensure that there are always 2 coins in the game
class CoinSystem(gamma.System):

    def update(self, scene):

        # get the number of coin entities in the scene
        num = len(scene.getEntitiesByTag('coin'))
        
        # create a new coin if there are less than 2
        if num < 2:
            
            # use the function stored in the entity factory to create a new coin
            # at a random position on the scene
            newCoin = gamma.entityFactory.create('coin', randint(-280, 280), randint(-180, 180))
            
            # add the new coin to the scene
            scene.addEntity(newCoin)
