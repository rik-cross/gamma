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
gamma.resourceManager.addImage('player', os.path.join('images', 'player', 'vita_00.png'))

#
# create a heart entity that moves automativcally
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(50, 50, 27, 30)
)
heartImage = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
heartEntity.getComponent('imagegroups').add('default', heartImage)

# heart movement = AI
def heartMovement(heart):
    if heart.getComponent('position').rect.x < 550:
        heart.getComponent('position').rect.x += 2

heartEntity.addComponent(gamma.InputComponent(inputContext=heartMovement))

#
# create a player entity that moves using WASD
#

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

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 200, 45, 51, xAnchor='center', yAnchor='middle'),
    gamma.ImageGroupsComponent('default', gamma.ImageGroup(gamma.resourceManager.getImage('player'))),
    gamma.InputComponent(up=gamma.keys.w, down=gamma.keys.s, left=gamma.keys.a, right=gamma.keys.d, inputContext=playerMovement)
)

#
# create a camera that has zoom functionality
#

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

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.BLUE),
    gamma.InputComponent(gamma.keys.up, gamma.keys.down, gamma.keys.left, gamma.keys.right, None, None, cameraMovement)
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