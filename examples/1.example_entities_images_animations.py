import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addImage('heart', os.path.join('images', 'heart.png'))

gamma.resourceManager.addImage('player_idle_1', os.path.join('images', 'player', 'vita_00.png'))
gamma.resourceManager.addImage('player_idle_2', os.path.join('images', 'player', 'vita_01.png'))
gamma.resourceManager.addImage('player_idle_3', os.path.join('images', 'player', 'vita_02.png'))
gamma.resourceManager.addImage('player_idle_4', os.path.join('images', 'player', 'vita_03.png'))

#
# create a heart entity
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(100, 100, 27, 30),
    gamma.ImageGroupsComponent('default', gamma.ImageGroup(gamma.resourceManager.getImage('heart')))
)

#
# create an animated player
#

playerAnimation = gamma.ImageGroup(
        gamma.resourceManager.getImage('player_idle_1'),
        gamma.resourceManager.getImage('player_idle_2'),
        gamma.resourceManager.getImage('player_idle_3'),
        gamma.resourceManager.getImage('player_idle_4')
    )

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 100, 45, 51),
    gamma.ImageGroupsComponent('default', playerAnimation)
)

#
# create a camera
#

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.BLUE)
)
cameraEntity.getComponent('camera').setPosition(300, 200)

#
# add entities to scene
#

mainScene.entities.append(heartEntity)
mainScene.entities.append(playerEntity)
mainScene.entities.append(cameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Image and Animation Example')
gamma.sceneManager.push(mainScene)
gamma.run()