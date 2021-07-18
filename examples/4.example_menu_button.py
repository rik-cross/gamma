import gamma

#
# create some functions to attach to the menu buttons
#

def changeTextColour():
    if mainScene.textColour == gamma.WHITE:
        mainScene.textColour = gamma.LIGHT_GREY
    else:
        mainScene.textColour = gamma.WHITE

def changeBackgroundColour():
    if mainScene.backgroundColour == gamma.BLUE:
        mainScene.backgroundColour = gamma.DARK_GREY
    else:
        mainScene.backgroundColour = gamma.BLUE

#
# create a main scene
#

class MainScene(gamma.Scene):

    def init(self):
        self.textColour = gamma.WHITE
        self.backgroundColour = gamma.BLUE
        self.setMenu(gamma.Menu(300,150,
            [
                gamma.ButtonUI('Change text colour', actionListener=gamma.ActionListener(changeTextColour)),
                gamma.ButtonUI('Change background colour', actionListener=gamma.ActionListener(changeBackgroundColour))
            ]
        ), self)

    def draw(self):
        self.surface.fill(self.backgroundColour)
        gamma.drawText(self.surface, 'Choose an option:', 25, 25, self.textColour, 255)

#
# add scene to the engine and start
#

mainScene = MainScene()
gamma.init((600, 400), caption='Gamma // Menu and Button Example')
gamma.sceneManager.push(mainScene)
gamma.run()