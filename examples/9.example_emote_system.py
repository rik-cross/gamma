import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

texturePlayer = gamma.createTexture(os.path.join('images', 'player', 'vita_00.png'))
textureHeart = gamma.createTexture(os.path.join('images', 'heart.png'))

#
# create a player entity
#

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 200, 45, 51, xAnchor='center', yAnchor='middle'),
    gamma.SpritesComponent('default', gamma.Sprite(texturePlayer)),
    # add a text component to the player entity
    gamma.EmoteComponent(textureHeart)
)

#
# create a camera
#

camera = gamma.Camera(0, 0, 600, 400,
    bgColour=gamma.BLUE,
    sceneX=300, sceneY = 150,
    zoomLevel = 2
)

#
# add entities to scene's world
#

mainScene.entities.append(playerEntity)

#
# add camera
#

mainScene.cameras.append(camera)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Emote System Example')
gamma.sceneManager.push(mainScene)
gamma.run()