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

#
# create a player entity
#

playerEntity = gamma.Entity(
    gamma.PositionComponent(0, 0, 45, 51),
    gamma.ColliderComponent(0,0,10,10)
)
playerAnimation = gamma.ImageGroup(
        gamma.resourceManager.getImage('player_idle_1')
    )
playerEntity.getComponent('imagegroups').add('idle', playerAnimation)
# triggers only work on entities with a collider
playerEntity.addComponent(gamma.ColliderComponent(0, 0, 45, 51))

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE
))

# player controls = enter to start cutscene
def playerControls(player):
    if gamma.inputManager.isDown(player.getComponent('input').left):
        player.getComponent('position').rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent('input').right):
        player.getComponent('position').rect.x += 2

playerEntity.addComponent(gamma.InputComponent(
    left=gamma.keys.a, right=gamma.keys.d,
    inputContext=playerControls)
)

# ensure the player is in front of the hearts
playerEntity.z = 10

#
# create a trigger to collect hearts
#

# create a trigger subclass for collecting a heart

class CollectHeartTrigger(gamma.Trigger):
    def onCollide(self, entity, otherEntity):
        if otherEntity.getComponent('tags').has('player'):
            mainScene.world.deleteEntity(entity)
            otherEntity.getComponent('inventory').addEntity('heart')

# add a heart to the entity factory

def createHeart(x, y):
    heartEntity = gamma.Entity()
    heartEntity.addComponent(gamma.PositionComponent(x, y, 27, 30))
    heartEntity.addComponent(gamma.TriggersComponent())
    heartEntity.getComponent('triggers').addTrigger(CollectHeartTrigger(boundingBox=gamma.PositionComponent(0,0,27,30), buttonPress=gamma.keys.w))
    heartImageGroup = gamma.ImageGroup(gamma.resourceManager.getImage('heart'))
    heartEntity.getComponent('imagegroups').add('idle', heartImageGroup)
    return heartEntity

gamma.entityFactory.addEntity('heart', createHeart)

# add some hearts to the player inventory
for i in range(15):
    playerEntity.getComponent('inventory').addEntity('heart')

# add a heart to the world
he = gamma.entityFactory.create('heart', 50, 0)
mainScene.world.entities.append(he)

#
# crafting
#

recipe = gamma.CraftingRecipe(
    'heart',
    ('heart', 1),
    ('heart', 2),
    ('heart', 3)
)
playerEntity.getComponent('crafting').addRecipe(recipe)

#
# add entities to scene's world
#

mainScene.world.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Lighting Example')
gamma.sceneManager.push(mainScene)
gamma.run()