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
textureHeart = gamma.createTexture(os.path.join('images', 'heart.png'))

#
# create a heart entity
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(300, 0, 27, 30)
)
heartImage = gamma.Sprite(textureHeart)
heartEntity.getComponent(gamma.SpritesComponent).add('default', heartImage)

# create a trigger subclass for focusing on the heart
class HeartFocusTrigger(gamma.Trigger):
    def onCollisionEnter(self, entity, otherEntity):
        camera.trackEntity(entity)
    def onCollide(self, entity, otherEntity):
        pass
    def onCollisionExit(self, entity, otherEntity):
        camera.trackEntity(otherEntity)

# create a trigger subclass for zooming in on the heart
class HeartZoomTrigger(gamma.Trigger):
    def onCollisionEnter(self, entity, otherEntity):
        camera.setZoom(4, duration=60)
    def onCollide(self, entity, otherEntity):
        pass
    def onCollisionExit(self, entity, otherEntity):
        camera.setZoom(1, duration=60)

# add triggers
heartEntity.addComponent(gamma.TriggersComponent())
heartEntity.getComponent(gamma.TriggersComponent).addTrigger(HeartFocusTrigger(boundingBox=gamma.PositionComponent(-100,-100,200,200)))
heartEntity.getComponent(gamma.TriggersComponent).addTrigger(HeartZoomTrigger(boundingBox=gamma.PositionComponent(0,0,27,30)))

#
# create a player entity
#

# player controls = enter to start cutscene
def playerControls(player):
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).left):
        player.getComponent(gamma.PositionComponent).rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).right):
        player.getComponent(gamma.PositionComponent).rect.x += 2

playerEntity = gamma.Entity(
    gamma.PositionComponent(0, 0, 45, 51),
    gamma.SpritesComponent('default', gamma.Sprite(texturePlayer)),
    # triggers only work on entities with a collider
    gamma.ColliderComponent(0, 0, 45, 51),
    gamma.InputComponent(left=gamma.keys.left, right=gamma.keys.right, inputContext=playerControls)
)

# create a camera
camera = gamma.Camera(
    0, 0, 600, 400,
    bgColour = gamma.BLUE,
    entityToTrack=playerEntity
)

#
# add entities to scene
#

mainScene.entities.append(playerEntity)
mainScene.entities.append(heartEntity)

#
# add camera
#

mainScene.cameras.append(camera)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Triggers Example')
gamma.sceneManager.push(mainScene)
gamma.run()