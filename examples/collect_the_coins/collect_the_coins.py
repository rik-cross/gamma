import gamma
import os
from scene_menu import MenuScene
from system_coin import CoinSystem
from factory_coin import newCoin

# add image resources to the resource manager

# Dinosaur player images by Arks: https://arks.itch.io/dino-characters
gamma.resourceManager.addImage('player', os.path.join('images', 'player', 'player.png'))

# Coin sprite by DasBilligeAlien: https://opengameart.org/content/rotating-coin-0
gamma.resourceManager.addImage('coin0', os.path.join('images', 'coin', 'coin_0.png'))
gamma.resourceManager.addImage('coin1', os.path.join('images', 'coin', 'coin_1.png'))
gamma.resourceManager.addImage('coin2', os.path.join('images', 'coin', 'coin_2.png'))
gamma.resourceManager.addImage('coin3', os.path.join('images', 'coin', 'coin_3.png'))
gamma.resourceManager.addImage('coin4', os.path.join('images', 'coin', 'coin_4.png'))
gamma.resourceManager.addImage('coin5', os.path.join('images', 'coin', 'coin_5.png'))

# add sound and music to the sound manager

# Music by ArcOfDream: https://arcofdream.itch.io/monolith-ost
gamma.soundManager.addMusic('solace', os.path.join('music', 'solace.ogg'))
gamma.soundManager.addMusic('dawn', os.path.join('music', 'before_the_dawn.ogg'))

# Sound by Maskedsound: https://maskedsound.itch.io/8-bit-sfx-pack
gamma.soundManager.addSound('coin', os.path.join('sounds', 'coin.ogg'))

# add a coin system to the list of systems
coinSystem = CoinSystem()
gamma.systemManager.addSystem(coinSystem)

# add a function to the entity factory for creating new coins
gamma.entityFactory.addEntity('coin', newCoin)

# initialise gamma
gamma.init(size=(600,400), caption='Collect the coins')

# add a menu scene to the sceneManager
gamma.sceneManager.push(MenuScene())

# start the game
gamma.run()