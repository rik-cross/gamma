import gamma

# create a player input context
# linking input to actions
def playerInputContext(player):

    # store some components, just to make the code easier to read!
    inputComponent = player.getComponent(gamma.InputComponent)
    positionComponent = player.getComponent(gamma.PositionComponent)

    # only proceed if entity has the required components
    if inputComponent is None or positionComponent is None:
        return
    
    # input associated with directions moves the player
    if gamma.inputManager.isDown(inputComponent.up):
        positionComponent.y -= 2
    if gamma.inputManager.isDown(inputComponent.down):
        positionComponent.y += 2
    if gamma.inputManager.isDown(inputComponent.left):
        positionComponent.x -= 2
    if gamma.inputManager.isDown(inputComponent.right):
        positionComponent.x += 2