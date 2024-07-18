import gamma
import os

#
# add images
#

texturePlayer = gamma.createTexture(os.path.join('images', 'player', 'vita_00.png'))

textureTileGrass = gamma.createTexture(os.path.join('images', 'textures/grass.png'))
textureTileDirt = gamma.createTexture(os.path.join('images', 'textures/dirt.png'))

textureBack = gamma.createTexture(os.path.join('images', 'layers/back.png'))
textureMiddle = gamma.createTexture(os.path.join('images', 'layers/middle.png'))
textureFront = gamma.createTexture(os.path.join('images', 'layers/front.png'))
textureForeground = gamma.createTexture(os.path.join('images', 'layers/foreground.png'))

#
# add some tiles
#

gamma.tileManager.addTile(gamma.Tile('grass', textureTileGrass, True))
gamma.tileManager.addTile(gamma.Tile('dirt', textureTileDirt, True))

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add map and scene images
#

mainScene.map = gamma.Map()
for i in range(20):
    mainScene.map.setTile(i,2,'grass')
    mainScene.map.setTile(i,3,'dirt')

mainScene.map.mapImages = [

    # mountains behind

    gamma.Image(textureBack,
    -100, 64,
    h=200,
    vAlign='bottom',
    z=0.2,
    xParallax=True),

    gamma.Image(textureMiddle,
    -100, 64,
    h=200,
    vAlign='bottom',
    z=0.4,
    xParallax=True),

    gamma.Image(textureFront,
    -100, 64,
    h=200,
    vAlign='bottom',
    z=0.6,
    xParallax=True),

    # tree trunk in front

    gamma.Image(textureForeground,
        600, 250,
        h=500,
        vAlign='bottom',
        z=3,
        xParallax=True)

]

#
# create a player entity
#

# player controls
def playerControls(player):
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).left):
        player.getComponent(gamma.PositionComponent).rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).right):
        player.getComponent(gamma.PositionComponent).rect.x += 2

playerEntity = gamma.Entity(
    gamma.PositionComponent(150, 64-51, 45, 51),
    gamma.SpritesComponent('default', gamma.Sprite(texturePlayer)),
    gamma.InputComponent(
        left=gamma.keys.a, right=gamma.keys.d,
        up=gamma.keys.w, down=gamma.keys.s,
        inputContext=playerControls
    ),
    gamma.ColliderComponent(0,0,10,10)
)

# add a camera to the player

playerEntity.addComponent(
    gamma.CameraComponent(
        0, 0, 600, 400,
        bgColour = gamma.BLUE,
        entityToTrack=playerEntity,
        clampToMap=False
    )
)

#
# add player to scene
#

mainScene.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Scene Images Example')
gamma.sceneManager.push(mainScene)
gamma.run()