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
    gamma.Position(100, 200, 27, 30)
)
heartImage = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
heartEntity.getComponent('imagegroups').add('idle', heartImage)

#
# create an animated player
#

playerEntity = gamma.Entity(
    gamma.Position(250, 200, 45, 51)
)
playerAnimation = gamma.ImageGroup(
        gamma.resourceManager.getImage('player_idle_1'),
        gamma.resourceManager.getImage('player_idle_2'),
        gamma.resourceManager.getImage('player_idle_3'),
        gamma.resourceManager.getImage('player_idle_4')
    )
playerEntity.getComponent('imagegroups').add('idle', playerAnimation)

#
# create some cameras
#

# world camera

worldCameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 400, 400, bgColour=gamma.BLUE)
)
worldCameraEntity.getComponent('camera').setPosition(200, 200)

# heart camera

heartCameraEntity = gamma.Entity(
    gamma.CameraComponent(400, 0, 200, 200, bgColour=gamma.RED)
)
heartCameraEntity.getComponent('camera').goToEntity(heartEntity)
heartCameraEntity.getComponent('camera').setZoom(5, duration=300)

# player camera

playerCameraEntity = gamma.Entity(
    gamma.CameraComponent(400, 200, 200, 200,bgColour=gamma.GREEN)
)
playerCameraEntity.getComponent('camera').trackEntity(playerEntity)
playerCameraEntity.getComponent('camera').setZoom(3)

#
# add entities to scene's world
#

# game entities

mainScene.world.entities.append(heartEntity)
mainScene.world.entities.append(playerEntity)

# cameras

mainScene.world.entities.append(worldCameraEntity)
mainScene.world.entities.append(heartCameraEntity)
mainScene.world.entities.append(playerCameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Camera Example')
gamma.sceneManager.push(mainScene)
gamma.run()