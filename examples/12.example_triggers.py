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
gamma.resourceManager.addTexture('player_idle_1', os.path.join('images', 'player', 'vita_00.png'))

#
# create a heart entity
#

heartEntity = gamma.Entity(
    gamma.PositionComponent(300, 0, 27, 30)
)
heartImage = gamma.Sprite(gamma.resourceManager.getTexture('heart'))
heartEntity.getComponent('sprites').add('default', heartImage)

# create a trigger subclass for focusing on the heart
class HeartFocusTrigger(gamma.Trigger):
    def onCollisionEnter(self, entity, otherEntity):
        otherEntity.getComponent('camera').trackEntity(entity)
    def onCollide(self, entity, otherEntity):
        pass
    def onCollisionExit(self, entity, otherEntity):
        otherEntity.getComponent('camera').trackEntity(otherEntity)

# create a trigger subclass for zooming in on the heart
class HeartZoomTrigger(gamma.Trigger):
    def onCollisionEnter(self, entity, otherEntity):
        otherEntity.getComponent('camera').setZoom(4, duration=60)
    def onCollide(self, entity, otherEntity):
        pass
    def onCollisionExit(self, entity, otherEntity):
        otherEntity.getComponent('camera').setZoom(1, duration=60)

# add triggers
heartEntity.addComponent(gamma.TriggersComponent())
heartEntity.getComponent('triggers').addTrigger(HeartFocusTrigger(boundingBox=gamma.PositionComponent(-100,-100,200,200)))
heartEntity.getComponent('triggers').addTrigger(HeartZoomTrigger(boundingBox=gamma.PositionComponent(0,0,27,30)))

#
# create a player entity
#

# player controls = enter to start cutscene
def playerControls(player):
    if gamma.inputManager.isDown(player.getComponent('input').left):
        player.getComponent('position').rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent('input').right):
        player.getComponent('position').rect.x += 2

playerEntity = gamma.Entity(
    gamma.PositionComponent(0, 0, 45, 51),
    gamma.SpritesComponent('default', gamma.Sprite(gamma.resourceManager.getTexture('player_idle_1'))),
    # triggers only work on entities with a collider
    gamma.ColliderComponent(0, 0, 45, 51),
    gamma.InputComponent(left=gamma.keys.left, right=gamma.keys.right, inputContext=playerControls)
)

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE,
    entityToTrack=playerEntity
))

#
# add entities to scene
#

mainScene.entities.append(playerEntity)
mainScene.entities.append(heartEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Triggers Example')
gamma.sceneManager.push(mainScene)
gamma.run()