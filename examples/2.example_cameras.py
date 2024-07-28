import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

textureHeart = gamma.createTexture(os.path.join('images', 'heart.png'))

texturePlayer1 = gamma.createTexture(os.path.join('images', 'player', 'vita_00.png'))
texturePlayer2 = gamma.createTexture(os.path.join('images', 'player', 'vita_01.png'))
texturePlayer3 = gamma.createTexture(os.path.join('images', 'player', 'vita_02.png'))
texturePlayer4 = gamma.createTexture(os.path.join('images', 'player', 'vita_03.png'))

#
# create a heart entity
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(100, 200, 27, 30),
    gamma.SpritesComponent('default', gamma.Sprite(textureHeart))
)

#
# create an animated player
#

playerAnimation = gamma.Sprite(
        texturePlayer1, texturePlayer2, texturePlayer3, texturePlayer4
    )

playerEntity = gamma.Entity(
    gamma.PositionComponent(250, 200, 45, 51),
    gamma.SpritesComponent('default', playerAnimation)
)

#
# create some cameras
#

# scene camera

sceneCamera = gamma.Camera(0, 0, 400, 400, bgColour=gamma.BLUE)
sceneCamera.setPosition(200, 200)

# heart camera

heartCamera = gamma.Camera(400, 0, 200, 200, bgColour=gamma.RED)
heartCamera.goToEntity(heartEntity)
heartCamera.setZoom(5, duration=300)

# player camera

playerCamera = gamma.Camera(400, 200, 200, 200,bgColour=gamma.GREEN)
playerCamera.trackEntity(playerEntity)
playerCamera.setZoom(3)

#
# add entities to scene
#

# game entities

mainScene.entities.append(heartEntity)
mainScene.entities.append(playerEntity)

# cameras

#mainScene.entities.append(sceneCameraEntity)
#mainScene.entities.append(heartCameraEntity)
#mainScene.entities.append(playerCameraEntity)

mainScene.cameras.append(sceneCamera)
mainScene.cameras.append(playerCamera)
mainScene.cameras.append(heartCamera)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Camera Example')
gamma.sceneManager.push(mainScene)
gamma.run()