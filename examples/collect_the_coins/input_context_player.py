import gamma

# create a player input context
# linking input to actions
def playerInputContext(player):

    # store some components, just to make the code easier to read!
    inp = player.getComponent('input')
    pos = player.getComponent('position')

    # only proceed if entity has the required components
    if inp is None or pos is None:
        return
    
    # input associated with directions moves the player
    if gamma.inputManager.isDown(inp.up):
        pos.y -= 2
    if gamma.inputManager.isDown(inp.down):
        pos.y += 2
    if gamma.inputManager.isDown(inp.left):
        pos.x -= 2
    if gamma.inputManager.isDown(inp.right):
        pos.x += 2