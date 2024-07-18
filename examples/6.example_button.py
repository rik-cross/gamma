import gamma
import os

#
# create a player entity to control the button
#

playerEntity = gamma.Entity()
playerEntity.addComponent(gamma.InputComponent(b1=gamma.keys.enter))

# store images

textureXOff = gamma.createTexture(os.path.join('images', 'x_n.png'))
textureXOn1 = gamma.createTexture(os.path.join('images', 'x_y1.png'))
textureXOn2 = gamma.createTexture(os.path.join('images', 'x_y2.png'))

#
# create a main scene
#

class MainScene(gamma.Scene):

    def init(self):

        self.background = gamma.BLUE

        # create a button

        # default image group
        defaultSprite = gamma.Sprite(textureXOff)
        # pressed image group
        pressedSprite = gamma.Sprite(textureXOn1, textureXOn2)
        # button linked to:
        # -- controller[0] x button
        # -- player entity 'button 1' (set as 'enter' above)
        self.addButton(gamma.UIButton(200, 150, defaultSprite, pressedSprite, controlledBy=[gamma.controller[0].x, playerEntity.getComponent(gamma.InputComponent).b1], text='press me!'))

    def draw(self):
        self.renderer.add(gamma.Text(
            'Press keyboard [enter] or controller [x] to activate.',
            25, 25
        ))

#
# add scene to the engine and start
#

mainScene = MainScene()
gamma.init((600, 400), caption='Gamma // Button Example')
gamma.sceneManager.push(mainScene)
gamma.run()