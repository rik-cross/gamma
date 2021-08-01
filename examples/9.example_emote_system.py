import gamma

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addImage('player', 'images/player/vita_00.png')
gamma.resourceManager.addImage('heart', 'images/heart.png')

#
# create a player entity
#

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 200, 45, 51, xAnchor='center', yAnchor='middle')
)
playerImage = gamma.ImageGroup(gamma.resourceManager.getImage('player'))
playerEntity.getComponent('imagegroups').add('default', playerImage)

# add a text component to the player entity
playerEntity.addComponent(
    gamma.EmoteComponent(gamma.resourceManager.getImage('heart'))
)

#
# create a camera
#

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400,
        bgColour=gamma.BLUE,
        worldX=300, worldY = 150,
        zoomLevel = 2
    )
)

#
# add entities to scene's world
#

mainScene.world.entities.append(playerEntity)
mainScene.world.entities.append(cameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Emote System Example')
gamma.sceneManager.push(mainScene)
gamma.run()