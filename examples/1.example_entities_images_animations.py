import gamma

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addImage('heart', 'images/heart.png')

gamma.resourceManager.addImage('player_idle_1', 'images/player/vita_00.png')
gamma.resourceManager.addImage('player_idle_2', 'images/player/vita_01.png')
gamma.resourceManager.addImage('player_idle_3', 'images/player/vita_02.png')
gamma.resourceManager.addImage('player_idle_4', 'images/player/vita_03.png')

#
# create a heart entity
#

heartEntity = gamma.Entity(
    gamma.Position(100, 100, 27, 30)
)
heartImage = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
heartEntity.getComponent('imagegroups').add('default', heartImage)

#
# create an animated player
#

playerEntity = gamma.Entity(
    gamma.Position(300, 100, 45, 51)
)
playerAnimation = gamma.ImageGroup(
        gamma.resourceManager.getImage('player_idle_1'),
        gamma.resourceManager.getImage('player_idle_2'),
        gamma.resourceManager.getImage('player_idle_3'),
        gamma.resourceManager.getImage('player_idle_4')
    )
playerEntity.getComponent('imagegroups').add('idle', playerAnimation)

#
# create a camera
#

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.BLUE)
)
cameraEntity.getComponent('camera').setPosition(300, 200)

#
# add entities to scene's world
#

mainScene.world.entities.append(heartEntity)
mainScene.world.entities.append(playerEntity)
mainScene.world.entities.append(cameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Image and Animation Example')
gamma.sceneManager.push(mainScene)
gamma.run()