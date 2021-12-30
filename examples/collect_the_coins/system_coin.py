import gamma
from random import randint

# system to ensure that there are always 2 coins in the game
class CoinSystem(gamma.System):

    def init(self):
        # system referred to as 'coin'
        self.key = 'coin'

    def update(self, scene):

        # get the number of coin entities in the world
        num = len(scene.world.getEntitiesByTag('coin'))
        
        # create a new coin if there are less than 2
        if num < 2:
            
            # use the function stored in the entity factory to create a new coin
            # at a random position on the scene
            newCoin = gamma.entityFactory.create('coin', randint(-280, 280), randint(-180, 180))
            
            # add the new coin to the scene's world
            scene.world.addEntity(newCoin)
