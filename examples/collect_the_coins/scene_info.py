import gamma

class InfoScene(gamma.Scene):

    def init(self):
        self.background = gamma.CORNFLOWER_BLUE
    
    def update(self):
        
        # esc to quit
        if gamma.inputManager.isPressed(gamma.keys.esc):
            gamma.sceneManager.pop()
    
    def draw(self):

        # game info
        self.renderer.add(gamma.Text('Collect the coins', 20, 20, underline=True))
        self.renderer.add(gamma.Text('See how many coins you can collect in 15 seconds', 20, 60,))
        self.renderer.add(gamma.Text('WASD to move the player', 20, 100))
        
        # exit info
        self.renderer.add(gamma.Text('[esc] back', 20, gamma.windowSize.h - 20, vAlign='bottom', font=gamma.fontDefaultSmall))
