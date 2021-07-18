import gamma

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add images
#

gamma.resourceManager.addImage('tile_grass', 'images/textures/grass.png')
gamma.resourceManager.addImage('tile_water', 'images/textures/water.png')

#
# add some tiles
#

gamma.Tile.addTile('grass', gamma.Tile(gamma.resourceManager.getImage('tile_grass'), True))
gamma.Tile.addTile('water', gamma.Tile(gamma.resourceManager.getImage('tile_water'), False))

#
# create a map
#

map = gamma.Map(map=[ ['grass' for i in range(10)] for j in range(10) ])
map.setTile(3,3,'water')
mainScene.world.map = map

#
# create a camera
#

worldCameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.DARK_GREY)
)
worldCameraEntity.getComponent('camera').setPosition(300, 200)

#
# add camera to world
#

mainScene.world.entities.append(worldCameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Map Example')
gamma.sceneManager.push(mainScene)
gamma.run()