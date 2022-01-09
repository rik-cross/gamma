import gamma
import os

#
# add images
#

gamma.resourceManager.addImage('player_idle_1', os.path.join('images', 'player', 'vita_00.png'))

gamma.resourceManager.addImage('tile_grass', os.path.join('images', 'textures/grass.png'))
gamma.resourceManager.addImage('tile_dirt', os.path.join('images', 'textures/dirt.png'))

gamma.resourceManager.addImage('back', os.path.join('images', 'layers/back.png'))
gamma.resourceManager.addImage('middle', os.path.join('images', 'layers/middle.png'))
gamma.resourceManager.addImage('front', os.path.join('images', 'layers/front.png'))
gamma.resourceManager.addImage('foreground', os.path.join('images', 'layers/foreground.png'))

#
# add some tiles
#

gamma.tileManager.addTile(gamma.Tile('grass', gamma.resourceManager.getImage('tile_grass'), True))
gamma.tileManager.addTile(gamma.Tile('dirt', gamma.resourceManager.getImage('tile_dirt'), True))

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add map and world images
#

mainScene.world.map = gamma.Map()
for i in range(20):
    mainScene.world.map.setTile(i,2,'grass')
    mainScene.world.map.setTile(i,3,'dirt')

mainScene.world.map.mapImages = [

    # mountains behind

    gamma.Image(gamma.resourceManager.getImage('back'),
    -100, 64,
    h=200,
    vAlign='bottom',
    z=0.2,
    xParallax=True),

    gamma.Image(gamma.resourceManager.getImage('middle'),
    -100, 64,
    h=200,
    vAlign='bottom',
    z=0.4,
    xParallax=True),

    gamma.Image(gamma.resourceManager.getImage('front'),
    -100, 64,
    h=200,
    vAlign='bottom',
    z=0.6,
    xParallax=True),

    # tree trunk in front

    gamma.Image(gamma.resourceManager.getImage('foreground'),
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
    if gamma.inputManager.isDown(player.getComponent('input').left):
        player.getComponent('position').rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent('input').right):
        player.getComponent('position').rect.x += 2

playerEntity = gamma.Entity(
    gamma.PositionComponent(150, 64-51, 45, 51),
    gamma.ImageGroupsComponent('idle', gamma.ImageGroup(gamma.resourceManager.getImage('player_idle_1'))),
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
# add player to scene's world
#

mainScene.world.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // World Images Example')
gamma.sceneManager.push(mainScene)
gamma.run()