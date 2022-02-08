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

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 100, 45, 51),
    gamma.ImageGroupsComponent('default', playerAnimation)
)

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE,
    entityToTrack = playerEntity
))

cutscene = gamma.Cutscene()
cutscene.actionList = [
    lambda: playerEntity.getComponent('camera').setZoom(3, duration=60),
    lambda: mainScene.cutscene.setDelay(120),
    lambda: playerEntity.addComponent(gamma.TextComponent('Hello! How are you?', lifetime='timed', type='tick', final_display_time=120)),
    lambda: mainScene.cutscene.setDelay(300),
    lambda: playerEntity.getComponent('camera').setZoom(1, duration=60),
    lambda: mainScene.cutscene.setDelay(60)
]

# player controls = enter to start cutscene
def playerControls(player):
    if gamma.inputManager.isPressed(player.getComponent('input').b1):
        # start the cutscene
        cutscene.reset()
        mainScene.cutscene = cutscene

playerEntity.addComponent(gamma.InputComponent(b1=gamma.keys.enter, inputContext=playerControls))

#
# add entities to scene
#

mainScene.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Cutscene Example')
gamma.sceneManager.push(mainScene)
gamma.run()