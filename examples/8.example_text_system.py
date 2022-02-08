import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addTexture('player', os.path.join('images', 'player', 'vita_00.png'))

#
# create a player entity
#

playerEntity = gamma.Entity(
    gamma.PositionComponent(300, 200, 45, 51, xAnchor='center', yAnchor='middle'),
    gamma.SpritesComponent('default', gamma.Sprite(gamma.resourceManager.getTexture('player'))),
    # add a text component to the player entity
    gamma.TextComponent('Here is some sample text, split over multiple lines.', type='tick', lifetime='timed') 
)

#
# create a camera
#

cameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400,
        bgColour=gamma.BLUE,
        sceneX=300, sceneY = 150,
        zoomLevel = 2
    )
)

#
# add entities to scene's world
#

mainScene.world.entities.append(playerEntity)
mainScene.world.entities.append(cameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Text System Example')
gamma.sceneManager.push(mainScene)
gamma.run()