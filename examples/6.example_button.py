from gamma.ui_text import drawText
from gamma import controller
import gamma

#
# create a player entity to control the button
#

playerEntity = gamma.Entity()
playerEntity.addComponent(gamma.Input(gamma.keys.up, gamma.keys.down, gamma.keys.left, gamma.keys.right, gamma.keys.enter, None))

# store images

gamma.resourceManager.addImage('x', 'images/x_n.png')
gamma.resourceManager.addImage('x_pressed1', 'images/x_y1.png')
gamma.resourceManager.addImage('x_pressed2', 'images/x_y2.png')

#
# create a main scene
#

class MainScene(gamma.Scene):

    def init(self):
        self.textColour = gamma.WHITE
        self.backgroundColour = gamma.BLUE

        # create a button

        # default image group
        defaultImageGroup = gamma.ImageGroup(gamma.resourceManager.getImage('x'))
        # pressed image group
        pressedImageGroup = gamma.ImageGroup(gamma.resourceManager.getImage('x_pressed1'), gamma.resourceManager.getImage('x_pressed2'))
        # button linked to:
        # -- controller[0] x button
        # -- player entity 'button 1' (set as 'enter' above)
        self.button = gamma.UIButton(200, 150, defaultImageGroup, pressedImageGroup, controlledBy=[gamma.controller[0].x, playerEntity.getComponent('input').b1], text='press me!')
        
    def update(self):
        self.button.update()

    def draw(self):
        self.surface.fill(self.backgroundColour)
        self.button.draw(self.surface)
        gamma.drawText(self.surface, 'Press keyboard [enter] or controller [x] to activate.', 25, 25, self.textColour)

#
# add scene to the engine and start
#

mainScene = MainScene()
gamma.init((600, 400), caption='Gamma // Button Example')
gamma.sceneManager.push(mainScene)
gamma.run()