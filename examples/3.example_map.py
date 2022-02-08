import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add images
#

gamma.resourceManager.addTexture('tile_grass', os.path.join('images', 'textures/grass.png'))
gamma.resourceManager.addTexture('tile_water', os.path.join('images', 'textures/water.png'))

#
# add some tiles
#

gamma.tileManager.addTile(gamma.Tile('grass', gamma.resourceManager.getTexture('tile_grass'), True))
gamma.tileManager.addTile(gamma.Tile('water', gamma.resourceManager.getTexture('tile_water'), False))

#
# create a map and add to scene
#

mainScene.setMap(gamma.Map(tiles=[ ['grass' for i in range(10)] for j in range(10) ]))
#map = mainScene.loadMap('filename.extension')
mainScene.map.setTile(3,3,'water')

#
# create a camera
#

sceneCameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.DARK_GREY)
)
sceneCameraEntity.getComponent('camera').setPosition(300, 200)

#
# add camera to scene
#

mainScene.entities.append(sceneCameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Map Example')
gamma.sceneManager.push(mainScene)
#mainScene.saveMap(map, 'filename.extension')
gamma.run()