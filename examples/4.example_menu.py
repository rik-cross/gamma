import gamma

#
# create a player entity to control the menu
#

playerEntity = gamma.Entity()
playerEntity.addComponent(gamma.Input(gamma.keys.up, gamma.keys.down, gamma.keys.left, gamma.keys.right, gamma.keys.enter, None))

#
# create some functions to attach to the menu buttons
#

def changeTextColour():
    if mainScene.textColour == gamma.WHITE:
        mainScene.textColour = gamma.LIGHT_GREY
    else:
        mainScene.textColour = gamma.WHITE

def changeBackgroundColour(colour):
    mainScene.backgroundColour = colour

#
# create a main scene
#

class MainScene(gamma.Scene):

    def init(self):
        self.textColour = gamma.WHITE
        self.backgroundColour = gamma.BLUE
        self.setMenu(gamma.Menu(300,150,
            [
                gamma.UITextMenuItem('Change title text colour', actionListener=gamma.ActionListener(changeTextColour)),
                gamma.UITextMenuItem('Change background to Blue', actionListener=gamma.ActionListener(changeBackgroundColour, gamma.BLUE)),
                gamma.UITextMenuItem('Change background to Dark Grey', actionListener=gamma.ActionListener(changeBackgroundColour, gamma.DARK_GREY))
            ]
        , entities=[playerEntity]), self)

    def draw(self):
        self.surface.fill(self.backgroundColour)
        gamma.drawText(self.surface, 'Choose an option:', 25, 25, self.textColour)

#
# add scene to the engine and start
#

mainScene = MainScene()
gamma.init((600, 400), caption='Gamma // Menu Example')
gamma.sceneManager.push(mainScene)
gamma.run()