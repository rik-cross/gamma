import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add images
#

textureTileGrass = gamma.createTexture(os.path.join('images', 'textures/grass.png'))
textureTileWater = gamma.createTexture(os.path.join('images', 'textures/water.png'))

#
# add some tiles
#

gamma.tileManager.addTile(gamma.Tile('grass', textureTileGrass, True))
gamma.tileManager.addTile(gamma.Tile('water', textureTileWater, False))

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
sceneCameraEntity.getComponent(gamma.CameraComponent).setPosition(300, 200)

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