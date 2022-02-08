import gamma
from scene_info import InfoScene
from scene_game import GameScene

class MenuScene(gamma.Scene):
    
    def init(self):
        self.background = gamma.CORNFLOWER_BLUE
    
    def onEnter(self):
        gamma.soundManager.playMusicFade('solace')

    def update(self):

        # 'i' to see info
        if gamma.inputManager.isPressed(gamma.keys.i):
            gamma.sceneManager.push(InfoScene())

        # 'enter' to see instructions
        if gamma.inputManager.isPressed(gamma.keys.enter):
            gamma.sceneManager.push(GameScene())

        # 'esc' to quit
        if gamma.inputManager.isPressed(gamma.keys.esc):
            gamma.quit()

    def draw(self):

        # title
        self.renderer.add(
            gamma.Text('Collect the coins',
                gamma.windowSize.w/2, 30,
                hAlign='center',
                font=gamma.resourceManager.getFont('large')
            )
        )

        # instructions
        self.renderer.add(
            gamma.Text('[enter] play    [i] info    [esc] exit',
                gamma.windowSize.w/2, 350,
                hAlign='center'
            )
        )

        # circle
        self.renderer.add(
            gamma.Circle(
                gamma.windowSize.w/2, 225,
                100,
                hAlign='center', vAlign='middle',
                colour=gamma.BLUE
            )
        )

        # coin
        self.renderer.add(
            gamma.Image(gamma.resourceManager.getTexture('coin0'),
                gamma.windowSize.w/2, 225,
                hAlign='center', vAlign='middle',
                w=23*4, h=23*4
            )
        )
