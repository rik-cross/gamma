import gamma

class GameOverScene(gamma.Scene):

    def init(self):

        # set a black, semi-transparent background
        self.background = gamma.getAlphaColour(gamma.BLACK, 180)
        # draw the game scene below
        self.drawSceneBelow = True
        
        # create a 'game over' message
        self.gameOverText = gamma.Text('Game over',
            gamma.windowSize.w/2, gamma.windowSize.h/2,
            hAlign='center', vAlign='middle',
            font=gamma.resourceManager.getFont('large')
        )

        # create text displaying the final player score
        score = self.getEntitiesByTag('player')[0].getComponent('score').score
        self.scoreText = gamma.Text('You scored ' + str(score), 300, self.gameOverText.bottom + 10, hAlign='center', vAlign='middle')

    def update(self):

        # return to main menu if esc key pressed
        if gamma.inputManager.isPressed(gamma.keys.esc):
            # pop both this overlay scene and the game scene
            gamma.sceneManager.pop(2)
    
    def draw(self):
        
        # draw game over message
        self.renderer.add(self.gameOverText)
        self.renderer.add(self.scoreText)

        # draw back text
        self.renderer.add(
            gamma.Text('[esc] back', 20, gamma.windowSize.h - 20, vAlign='bottom', font=gamma.resourceManager.getFont('small'))
        )