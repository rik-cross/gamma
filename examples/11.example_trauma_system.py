import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addTexture('heart', os.path.join('images', 'heart.png'))

gamma.resourceManager.addTexture('player_idle_1', os.path.join('images', 'player', 'vita_00.png'))
gamma.resourceManager.addTexture('player_idle_2', os.path.join('images', 'player', 'vita_01.png'))
gamma.resourceManager.addTexture('player_idle_3', os.path.join('images', 'player', 'vita_02.png'))
gamma.resourceManager.addTexture('player_idle_4', os.path.join('images', 'player', 'vita_03.png'))

#
# create a heart entity
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(100, 100, 27, 30),
    gamma.ImageGroupsComponent('default', gamma.ImageGroup(gamma.resourceManager.getTexture('heart')))
)

#
# create an animated player
#

playerAnimation = gamma.ImageGroup(
        gamma.resourceManager.getTexture('player_idle_1'),
        gamma.resourceManager.getTexture('player_idle_2'),
        gamma.resourceManager.getTexture('player_idle_3'),
        gamma.resourceManager.getTexture('player_idle_4')
    )

# player controls = enter to add trauma
def playerControls(player):
    if gamma.inputManager.isPressed(player.getComponent('input').b1):
        pass
        # add some trauma
        player.getComponent('trauma').traumaLevel += 0.4

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 100, 45, 51),
    gamma.ImageGroupsComponent('default', playerAnimation),
    gamma.InputComponent(b1=gamma.keys.enter, inputContext=playerControls),
    # add a trauma component to the player
    gamma.TraumaComponent()
)

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE,
    zoomLevel = 2,
    entityToTrack = playerEntity
))

#
# add entities to scene
#

mainScene.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Trauma System Example')
gamma.sceneManager.push(mainScene)
gamma.run()