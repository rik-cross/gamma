import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addImage('player_idle_1', os.path.join('images', 'player', 'vita_00.png'))
gamma.resourceManager.addImage('heart', os.path.join('images', 'heart.png'))

#
# create a player entity
#

# player controls = enter to start cutscene
def playerControls(player):
    # left and right movement
    if gamma.inputManager.isDown(player.getComponent('input').left):
        player.getComponent('position').rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent('input').right):
        player.getComponent('position').rect.x += 2
    # inventory controls
    if gamma.inputManager.isPressed(player.getComponent('input').b1):
        player.getComponent('inventory').prev()
    if gamma.inputManager.isPressed(player.getComponent('input').b2):
        player.getComponent('inventory').next()
    # drop item
    if gamma.inputManager.isPressed(player.getComponent('input').down):
        entity = player.getComponent('inventory').dropItem()
        if entity is not None:
            pos = player.getComponent('position')
            entity.getComponent('position').center = pos.x + pos.w/2
            entity.getComponent('position').bottom = pos.y + pos.h
            mainScene.addEntity(entity)

playerEntity = gamma.Entity(
    gamma.TagsComponent('player'),
    gamma.PositionComponent(0, 0, 45, 51, z=10),
    gamma.ImageGroupsComponent('default', gamma.ImageGroup(gamma.resourceManager.getImage('player_idle_1'))),
    # triggers only work on entities with a collider
    gamma.ColliderComponent(0,0,45,51),
    gamma.InputComponent(
        left=gamma.keys.a, right=gamma.keys.d,
        up=gamma.keys.w, down=gamma.keys.s,
        b1=gamma.keys.q, b2=gamma.keys.e,
        inputContext=playerControls
    )
)

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE
))

playerEntity.addComponent(
    gamma.InventoryComponent(
        20, 20,
        slots=3
    )
)

#
# create a trigger to collect hearts
#

# create a trigger subclass for collecting a heart

class CollectHeartTrigger(gamma.Trigger):
    def onCollide(self, entity, otherEntity):
        if otherEntity.getComponent('tags').has('player'):
            entity.destroy()
            otherEntity.getComponent('inventory').addEntity('heart')

# add a heart to the entity factory

def createHeart(x, y):
    heartEntity = gamma.Entity()
    heartEntity.addComponent(gamma.PositionComponent(x, y, 27, 30))
    heartEntity.addComponent(gamma.TriggersComponent(CollectHeartTrigger(boundingBox=gamma.PositionComponent(0,0,27,30), buttonPress='b1')))
    heartImageGroup = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
    heartEntity.getComponent('imagegroups').add('idle', heartImageGroup)
    return heartEntity

gamma.entityFactory.addEntity('heart', createHeart)

# add some hearts to the player inventory
for i in range(5):
    playerEntity.getComponent('inventory').addEntity('heart')

# add a heart to the scene
he = gamma.entityFactory.create('heart', 50, 0)
mainScene.entities.append(he)

#
# add entities to scene
#

mainScene.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Inventory Example')
gamma.sceneManager.push(mainScene)
gamma.run()