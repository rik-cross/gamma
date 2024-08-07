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
# create a player entity
#

# player controls
def playerControls(player):
    # left and right movement
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).left):
        player.getComponent(gamma.PositionComponent).rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent(gamma.InputComponent).right):
        player.getComponent(gamma.PositionComponent).rect.x += 2
    # inventory controls
    if gamma.inputManager.isPressed(player.getComponent(gamma.InputComponent).b1):
        player.getComponent(gamma.InventoryComponent).prev()
    if gamma.inputManager.isPressed(player.getComponent(gamma.InputComponent).b2):
        player.getComponent(gamma.InventoryComponent).next()
    # drop item
    if gamma.inputManager.isPressed(player.getComponent(gamma.InputComponent).down):
        entity = player.getComponent(gamma.InventoryComponent).dropItem()
        if entity is not None:
            pos = player.getComponent(gamma.PositionComponent)
            entity.getComponent(gamma.PositionComponent).center = pos.x + pos.w/2
            entity.getComponent(gamma.PositionComponent).bottom = pos.y + pos.h
            mainScene.addEntity(entity)

playerEntity = gamma.Entity(
    gamma.TagsComponent('player'),
    gamma.PositionComponent(0, 0, 45, 51, z=10),
    gamma.SpritesComponent('default', gamma.Sprite(texturePlayer)),
    # triggers only work on entities with a collider
    gamma.ColliderComponent(0,0,45,51),
    gamma.InputComponent(
        left=gamma.keys.a, right=gamma.keys.d,
        up=gamma.keys.w, down=gamma.keys.s,
        b1=gamma.keys.q, b2=gamma.keys.e,
        inputContext=playerControls
    )
)

playerEntity.addComponent(
    gamma.InventoryComponent(
        20, 20,
        slots=3
    )
)

# create a camera
camera = gamma.Camera(
    0, 0, 600, 400,
    bgColour = gamma.BLUE
)

#
# create a trigger to collect hearts
#

# create a trigger subclass for collecting a heart

class CollectHeartTrigger(gamma.Trigger):
    def onCollide(self, entity, otherEntity):
        if otherEntity.getComponent(gamma.TagsComponent).has('player'):
            entity.destroy()
            otherEntity.getComponent(gamma.InventoryComponent).addEntity('heart')

# add a heart to the entity factory

def createHeart(x, y):
    heartEntity = gamma.Entity()
    heartEntity.addComponent(gamma.PositionComponent(x, y, 27, 30))
    heartEntity.addComponent(gamma.TriggersComponent(CollectHeartTrigger(boundingBox=gamma.PositionComponent(0,0,27,30), buttonPress='b1')))
    heartSprite = gamma.Sprite(textureHeart)
    heartEntity.getComponent(gamma.SpritesComponent).add('default', heartSprite)
    return heartEntity

gamma.entityFactory.addEntity('heart', createHeart)

# add some hearts to the player inventory
for i in range(5):
    playerEntity.getComponent(gamma.InventoryComponent).addEntity('heart')

# add a heart to the scene
he = gamma.entityFactory.create('heart', 50, 0)
mainScene.entities.append(he)

#
# add entities to scene
#

mainScene.entities.append(playerEntity)

#
# add a camera
#

mainScene.cameras.append(camera)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Inventory Example')
gamma.sceneManager.push(mainScene)
gamma.run()