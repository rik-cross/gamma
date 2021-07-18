import gamma

#
# create some functions to attach to the menu buttons
#

def pushSecond():
    #gamma.sceneManager.push(secondScene)
    gamma.sceneManager.setTransition(gamma.TransitionNone([firstScene],[secondScene]))

def blackTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionBlack([firstScene],[secondScene]))

def fadeTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionFade([firstScene],[secondScene]))

def wipeLeftTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionWipeLeft([firstScene],[secondScene]))

def wipeRightTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionWipeRight([firstScene],[secondScene]))

def flyOutLeftTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionFlyOutLeft([firstScene],[secondScene]))

def flyOutRightTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionFlyOutRight([firstScene],[secondScene]))

def flyInLeftTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionFlyInLeft([firstScene],[secondScene]))

def flyInRightTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionFlyInRight([firstScene],[secondScene]))

def moveLeftTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionMoveLeft([firstScene],[secondScene]))

def moveRightTransitionSecond():
    gamma.sceneManager.setTransition(gamma.TransitionMoveRight([firstScene],[secondScene]))

def popScene():
    #gamma.sceneManager.pop()
    gamma.sceneManager.setTransition(gamma.TransitionNone([secondScene],[]))

def blackTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionBlack([secondScene],[]))

def fadeTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionFade([secondScene],[]))

def wipeLeftTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionWipeLeft([secondScene],[]))

def wipeRightTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionWipeRight([secondScene],[]))

def flyOutLeftTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionFlyOutLeft([secondScene],[]))

def flyOutRightTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionFlyOutRight([secondScene],[]))

def flyInLeftTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionFlyInLeft([secondScene],[]))

def flyInRightTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionFlyInRight([secondScene],[]))

def moveLeftTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionMoveLeft([secondScene],[]))

def moveRightTransitionFirst():
    gamma.sceneManager.setTransition(gamma.TransitionMoveRight([secondScene],[]))

#
# create scenes
#

class FirstScene(gamma.Scene):

    def init(self):
        self.setMenu(gamma.Menu(300,70,
            [
                gamma.ButtonUI('No transition', actionListener=gamma.ActionListener(pushSecond)),
                gamma.ButtonUI('Black transition', actionListener=gamma.ActionListener(blackTransitionSecond)),
                gamma.ButtonUI('Fade transition', actionListener=gamma.ActionListener(fadeTransitionSecond)),
                gamma.ButtonUI('Wipe left transition', actionListener=gamma.ActionListener(wipeLeftTransitionSecond)),
                gamma.ButtonUI('Wipe right transition', actionListener=gamma.ActionListener(wipeRightTransitionSecond)),
                gamma.ButtonUI('Fly out left transition', actionListener=gamma.ActionListener(flyOutLeftTransitionSecond)),
                gamma.ButtonUI('Fly out right transition', actionListener=gamma.ActionListener(flyOutRightTransitionSecond)),
                gamma.ButtonUI('Fly in left transition', actionListener=gamma.ActionListener(flyInLeftTransitionSecond)),
                gamma.ButtonUI('Fly in right transition', actionListener=gamma.ActionListener(flyInRightTransitionSecond)),
                gamma.ButtonUI('Move left transition', actionListener=gamma.ActionListener(moveLeftTransitionSecond)),
                gamma.ButtonUI('Move right transition', actionListener=gamma.ActionListener(moveRightTransitionSecond)),
                gamma.ButtonUI('Quit', actionListener=gamma.ActionListener(popScene))
            ]
        , spacing=25), self)

    def draw(self):
        self.surface.fill(gamma.BLUE)
        gamma.drawText(self.surface, 'First scene. Move to second scene using...', 25, 25, gamma.WHITE, 255)

class SecondScene(gamma.Scene):

    def init(self):
        self.setMenu(gamma.Menu(300,70,
            [
                gamma.ButtonUI('No transition', actionListener=gamma.ActionListener(popScene)),
                gamma.ButtonUI('Black transition', actionListener=gamma.ActionListener(blackTransitionFirst)),
                gamma.ButtonUI('Fade transition', actionListener=gamma.ActionListener(fadeTransitionFirst)),
                gamma.ButtonUI('Wipe left transition', actionListener=gamma.ActionListener(wipeLeftTransitionFirst)),
                gamma.ButtonUI('Wipe right transition', actionListener=gamma.ActionListener(wipeRightTransitionFirst)),
                gamma.ButtonUI('Fly out left transition', actionListener=gamma.ActionListener(flyOutLeftTransitionFirst)),
                gamma.ButtonUI('Fly out right transition', actionListener=gamma.ActionListener(flyOutRightTransitionFirst)),
                gamma.ButtonUI('Fly in left transition', actionListener=gamma.ActionListener(flyInLeftTransitionFirst)),
                gamma.ButtonUI('Fly in right transition', actionListener=gamma.ActionListener(flyInRightTransitionFirst)),
                gamma.ButtonUI('Move left transition', actionListener=gamma.ActionListener(moveLeftTransitionFirst)),
                gamma.ButtonUI('Move right transition', actionListener=gamma.ActionListener(moveRightTransitionFirst))
            ]
        , spacing=25), self)
    
    def draw(self):
        self.surface.fill(gamma.RED)
        gamma.drawText(self.surface, 'Second scene. Back to first scene using...', 25, 25, gamma.WHITE, 255)
 
firstScene = FirstScene()
secondScene = SecondScene()

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Scenes and Transitions Example')
gamma.sceneManager.push(firstScene)
gamma.run()