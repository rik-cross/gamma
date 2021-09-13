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
    gamma.PositionComponent(100, 100, 27, 30)
)
heartImage = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
heartEntity.getComponent('imagegroups').add('default', heartImage)

#
# create an animated player
#

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 100, 45, 51),
    gamma.TraumaComponent()
)
playerAnimation = gamma.ImageGroup(
        gamma.resourceManager.getImage('player_idle_1'),
        gamma.resourceManager.getImage('player_idle_2'),
        gamma.resourceManager.getImage('player_idle_3'),
        gamma.resourceManager.getImage('player_idle_4')
    )
playerEntity.getComponent('imagegroups').add('idle', playerAnimation)

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE,
    zoomLevel = 2,
    entityToTrack = playerEntity
))

# player controls = enter to add trauma
def playerControls(player):
    if gamma.inputManager.isPressed(player.getComponent('input').b1):
        pass
        # add some trauma
        player.getComponent('trauma').traumaLevel += 0.4

playerEntity.addComponent(gamma.InputComponent(b1=gamma.keys.enter, inputContext=playerControls))

#
# add entities to scene's world
#

mainScene.world.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Trauma System Example')
gamma.sceneManager.push(mainScene)
gamma.run()