import gamma
import os

#
# create a player entity to control the button
#

playerEntity = gamma.Entity()
playerEntity.addComponent(gamma.InputComponent(b1=gamma.keys.enter))

# store images

gamma.resourceManager.addImage('x', os.path.join('images', 'x_n.png'))
gamma.resourceManager.addImage('x_pressed1', os.path.join('images', 'x_y1.png'))
gamma.resourceManager.addImage('x_pressed2', os.path.join('images', 'x_y2.png'))

#
# create a main scene
#

class MainScene(gamma.Scene):

    def init(self):

        # create a button

        # default image group
        defaultImageGroup = gamma.ImageGroup(gamma.resourceManager.getImage('x'))
        # pressed image group
        pressedImageGroup = gamma.ImageGroup(gamma.resourceManager.getImage('x_pressed1'), gamma.resourceManager.getImage('x_pressed2'))
        # button linked to:
        # -- controller[0] x button
        # -- player entity 'button 1' (set as 'enter' above)
        self.addButton(gamma.UIButton(200, 150, defaultImageGroup, pressedImageGroup, controlledBy=[gamma.controller[0].x, playerEntity.getComponent('input').b1], text='press me!'))

    def draw(self):
        self.surface.fill(gamma.BLUE)
        gamma.Text(
            'Press keyboard [enter] or controller [x] to activate.',
            25, 25
        ).draw(self.surface)

#
# add scene to the engine and start
#

mainScene = MainScene()
gamma.init((600, 400), caption='Gamma // Button Example')
gamma.sceneManager.push(mainScene)
gamma.run()