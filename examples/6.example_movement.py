from gamma import inputmanager
import gamma

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addImage('heart', 'images/heart.png')
gamma.resourceManager.addImage('player', 'images/player/vita_00.png')

#
# create a heart entity that moves automativcally
#

heartEntity = gamma.Entity(
    gamma.Position(50, 50, 27, 30)
)
heartImage = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
heartEntity.getComponent('imagegroups').add('idle', heartImage)

#
# create a player entity that moves using WASD
#

playerEntity = gamma.Entity(
    gamma.Position(300, 300, 45, 51)
)
playerImage = gamma.ImageGroup(gamma.resourceManager.getImage('player'))
playerEntity.getComponent('imagegroups').add('idle', playerImage)

def playerMovement(player):
    if gamma.inputManager.isDown(player.getComponent('input').up):
        print('up')
        player.getComponent('transform')
    if gamma.inputManager.isDown(player.getComponent('input').down):
        print('down')
    if gamma.inputManager.isDown(player.getComponent('input').left):
        print('left')
    if gamma.inputManager.isDown(player.getComponent('input').right):
        print('right')

playerEntity.addComponent(gamma.Input(gamma.keys.w, gamma.keys.s, gamma.keys.a, gamma.keys.d, None, None, playerMovement))

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