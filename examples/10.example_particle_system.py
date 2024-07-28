import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

texturePlayer = gamma.createTexture(os.path.join('images', 'player', 'vita_00.png'))

#
# create a player entity that moves using WASD
#

# player controls = WASD keys, enter to create a particle emitter
def playerControls(player):
    
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).up):
        player.getComponent(gamma.PositionComponent).y -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).down):
        player.getComponent(gamma.PositionComponent).y += 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).left):
        player.getComponent(gamma.PositionComponent).x -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).right):
        player.getComponent(gamma.PositionComponent).x += 2
    
    if gamma.inputManager.isPressed(player.getComponent(gamma.InputComponent).b1):
        # add a new particle emitter at the player's center position
        player.addComponent(
            gamma.ParticleEmitterComponent(
                xOff=(player.getComponent(gamma.PositionComponent).w/2),
                yOff=(player.getComponent(gamma.PositionComponent).h/2)
            )
        )

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 200, 45, 51, xAnchor='center', yAnchor='middle'),
    gamma.SpritesComponent('default', gamma.Sprite(texturePlayer)),
    gamma.InputComponent(up=gamma.keys.w, down=gamma.keys.s, left=gamma.keys.a, right=gamma.keys.d, b1=gamma.keys.enter, inputContext=playerControls)
)

#
# create a camera
#

camera = gamma.Camera(0, 0, 600, 400,
    bgColour = gamma.BLUE,
    sceneX = 300, sceneY = 200
)

#
# add entities to scene
#

mainScene.entities.append(playerEntity)

#
# add camera
#

mainScene.cameras.append(camera)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Particle System Example')
gamma.sceneManager.push(mainScene)
gamma.run()