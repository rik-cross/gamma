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

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE,
    entityToTrack = playerEntity
))

cutscene = gamma.Cutscene()
cutscene.actionList = [
    lambda: playerEntity.getComponent(gamma.CameraComponent).setZoom(3, duration=60),
    lambda: mainScene.cutscene.setDelay(120),
    lambda: playerEntity.addComponent(gamma.TextComponent('Hello! How are you?', lifetime='timed', type='tick', final_display_time=120)),
    lambda: mainScene.cutscene.setDelay(300),
    lambda: playerEntity.getComponent(gamma.CameraComponent).setZoom(1, duration=60),
    lambda: mainScene.cutscene.setDelay(60)
]

# player controls = enter to start cutscene
def playerControls(player):
    if gamma.inputManager.isPressed(player.getComponent(gamma.InputComponent).b1):
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