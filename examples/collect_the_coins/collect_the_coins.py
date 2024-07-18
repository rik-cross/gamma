import gamma
import os
from scene_menu import MenuScene
from system_coin import CoinSystem
from factory_coin import newCoin

# add sound and music to the sound manager

# Music by ArcOfDream: https://arcofdream.itch.io/monolith-ost
gamma.soundManager.addMusic('solace', os.path.join('music', 'solace.ogg'))
gamma.soundManager.addMusic('dawn', os.path.join('music', 'before_the_dawn.ogg'))

# Sound by Maskedsound: https://maskedsound.itch.io/8-bit-sfx-pack
gamma.soundManager.addSound('coin', os.path.join('sounds', 'coin.ogg'))

# add a custom coin system
coinSystem = CoinSystem()
gamma.systemManager.addSystem(coinSystem)

# initialise gamma
gamma.init(size=(600,400), caption='Collect the coins')

# add a menu scene to the sceneManager
gamma.sceneManager.push(MenuScene())

# start the game
gamma.run()