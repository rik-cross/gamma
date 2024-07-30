import gamma
from random import randint
from factory_coin import newCoin
from scene_game import GameScene

# system to ensure that there are always 2 coins in the game
class CoinSystem(gamma.System):

    def update(self, scene):

        # only update the coin system in the game scene
        
        if type(scene) is not GameScene:
            return

        # get the number of coin entities in the scene
        num = len(scene.getEntitiesByTag('coin'))
        
        # create a new coin if there are less than 2
        if num < 2:
            
            # use the function stored in the entity factory to create a new coin
            # at a random position on the scene
            newCoinEntity = newCoin(randint(-280, 280), randint(-180, 180))
            
            # add the new coin to the scene
            scene.addEntity(newCoinEntity)
