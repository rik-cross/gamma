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
heartEntity.getComponent('imagegroups').add('default', heartImage)

# heart movement = AI
def heartMovement(heart):
    if heart.getComponent('position').rect.x < 550:
        heart.getComponent('position').rect.x += 2

heartEntity.addComponent(gamma.Input(None, None, None, None, None, None, heartMovement))

#
# create a player entity that moves using WASD
#

playerEntity = gamma.Entity(
    gamma.Position(300, 200, 45, 51, xAnchor='center', yAnchor='middle')
)
playerImage = gamma.ImageGroup(gamma.resourceManager.getImage('player'))
playerEntity.getComponent('imagegroups').add('default', playerImage)

# player movement = WASD keys
def playerMovement(player):
    if gamma.inputManager.isDown(player.getComponent('input').up):
        player.getComponent('position').y -= 2
    if gamma.inputManager.isDown(player.getComponent('input').down):
        player.getComponent('position').y += 2
    if gamma.inputManager.isDown(player.getComponent('input').left):
        player.getComponent('position').x -= 2
    if gamma.inputManager.isDown(player.getComponent('input').right):
        player.getComponent('position').x += 2

playerEntity.addComponent(gamma.Input(gamma.keys.w, gamma.keys.s, gamma.keys.a, gamma.keys.d, None, None, playerMovement))

#
# create a camera that has zoom functionality
#

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.BLUE)
)
cameraEntity.getComponent('camera').setPosition(300, 200)

# camera movement = arrow keys up/down to zoom, left/right to pan
def cameraMovement(camera):
    # zoom
    if gamma.inputManager.isDown(camera.getComponent('input').up):
        camera.getComponent('camera').zoomLevel += 0.02
    if gamma.inputManager.isDown(camera.getComponent('input').down):
        camera.getComponent('camera').zoomLevel = max(camera.getComponent('camera').zoomLevel - 0.02, 0.1)
    # pan
    if gamma.inputManager.isDown(camera.getComponent('input').left):
        camera.getComponent('camera').worldX -= 2
    if gamma.inputManager.isDown(camera.getComponent('input').right):
        camera.getComponent('camera').worldX += 2

cameraEntity.addComponent(gamma.Input(gamma.keys.up, gamma.keys.down, gamma.keys.left, gamma.keys.right, None, None, cameraMovement))

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