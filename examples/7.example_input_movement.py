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
gamma.resourceManager.addTexture('player', os.path.join('images', 'player', 'vita_00.png'))

#
# create a heart entity that moves automativcally
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(50, 50, 27, 30)
)
heartImage = gamma.Sprite(gamma.resourceManager.getTexture('heart'))
heartEntity.getComponent(gamma.SpritesComponent).add('default', heartImage)

# heart movement = AI
def heartMovement(heart):
    if heart.getComponent(gamma.PositionComponent).rect.x < 550:
        heart.getComponent(gamma.PositionComponent).rect.x += 2

heartEntity.addComponent(gamma.InputComponent(inputContext=heartMovement))

#
# create a player entity that moves using WASD
#

# player movement = WASD keys
def playerMovement(player):
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).up):
        player.getComponent(gamma.PositionComponent).y -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).down):
        player.getComponent(gamma.PositionComponent).y += 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).left):
        player.getComponent(gamma.PositionComponent).x -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).right):
        player.getComponent(gamma.PositionComponent).x += 2

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 200, 45, 51, xAnchor='center', yAnchor='middle'),
    gamma.SpritesComponent('default', gamma.Sprite(gamma.resourceManager.getTexture('player'))),
    gamma.InputComponent(up=gamma.keys.w, down=gamma.keys.s, left=gamma.keys.a, right=gamma.keys.d, inputContext=playerMovement)
)

#
# create a camera that has zoom functionality
#

# camera movement = arrow keys up/down to zoom, left/right to pan
def cameraMovement(camera):
    # zoom
    if gamma.inputManager.isDown(camera.getComponent(gamma.InputComponent).up):
        camera.getComponent(gamma.CameraComponent).zoomLevel += 0.02
    if gamma.inputManager.isDown(camera.getComponent(gamma.InputComponent).down):
        camera.getComponent(gamma.CameraComponent).zoomLevel = max(camera.getComponent(gamma.CameraComponent).zoomLevel - 0.02, 0.1)
    # pan
    if gamma.inputManager.isDown(camera.getComponent(gamma.InputComponent).left):
        camera.getComponent(gamma.CameraComponent).sceneX -= 2
    if gamma.inputManager.isDown(camera.getComponent(gamma.InputComponent).right):
        camera.getComponent(gamma.CameraComponent).sceneX += 2

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.BLUE),
    gamma.InputComponent(gamma.keys.up, gamma.keys.down, gamma.keys.left, gamma.keys.right, None, None, cameraMovement)
)
cameraEntity.getComponent(gamma.CameraComponent).setPosition(300, 200)

#
# add entities to scene
#

mainScene.entities.append(heartEntity)
mainScene.entities.append(playerEntity)
mainScene.entities.append(cameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Image and Animation Example')
gamma.sceneManager.push(mainScene)
gamma.run()