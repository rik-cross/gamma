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
    gamma.PositionComponent(100, 100, 27, 30),
    gamma.SpritesComponent('default', gamma.Sprite(textureHeart))
)

#
# create an animated player
#

playerAnimation = gamma.Sprite(
    texturePlayer1, texturePlayer2, texturePlayer3, texturePlayer4
)

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 100, 45, 51),
    gamma.SpritesComponent('default', playerAnimation)
)

#
# create a camera
#

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.BLUE)
)
cameraEntity.getComponent(gamma.CameraComponent).setPosition(300, 200)

#
# add entities to scene
#

mainScene.entities.append(heartEntity)
mainScene.entities.append(playerEntity)
mainScene.entities.append(cameraEntity)

#heartEntity.getComponent(gamma.TagsComponent).add('heart')

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Image and Animation Example')
gamma.sceneManager.push(mainScene)
gamma.run()