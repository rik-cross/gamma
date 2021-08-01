import gamma

#
# create a player entity to control the menu
#

playerEntity = gamma.Entity()
playerEntity.addComponent(gamma.InputComponent(gamma.keys.up, gamma.keys.down, gamma.keys.left, gamma.keys.right, gamma.keys.enter, None))
# optionally store the entity in the entityManager
playerEntity.getComponent('tags').add('player')
gamma.entityManager.addEntity(playerEntity)

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
                gamma.UITextMenuItem('No transition', actionListener=gamma.ActionListener(pushSecond)),
                gamma.UITextMenuItem('Black transition', actionListener=gamma.ActionListener(blackTransitionSecond)),
                gamma.UITextMenuItem('Fade transition', actionListener=gamma.ActionListener(fadeTransitionSecond)),
                gamma.UITextMenuItem('Wipe left transition', actionListener=gamma.ActionListener(wipeLeftTransitionSecond)),
                gamma.UITextMenuItem('Wipe right transition', actionListener=gamma.ActionListener(wipeRightTransitionSecond)),
                gamma.UITextMenuItem('Fly out left transition', actionListener=gamma.ActionListener(flyOutLeftTransitionSecond)),
                gamma.UITextMenuItem('Fly out right transition', actionListener=gamma.ActionListener(flyOutRightTransitionSecond)),
                gamma.UITextMenuItem('Fly in left transition', actionListener=gamma.ActionListener(flyInLeftTransitionSecond)),
                gamma.UITextMenuItem('Fly in right transition', actionListener=gamma.ActionListener(flyInRightTransitionSecond)),
                gamma.UITextMenuItem('Move left transition', actionListener=gamma.ActionListener(moveLeftTransitionSecond)),
                gamma.UITextMenuItem('Move right transition', actionListener=gamma.ActionListener(moveRightTransitionSecond)),
                gamma.UITextMenuItem('Quit', actionListener=gamma.ActionListener(popScene))
            ]
        , spacing=25, entities=gamma.entityManager.getEntitiesByTag('player')), self)

    def draw(self):
        self.surface.fill(gamma.BLUE)
        gamma.drawText(self.surface, 'First scene. Move to second scene using...', 25, 25, gamma.WHITE)

class SecondScene(gamma.Scene):

    def init(self):
        self.setMenu(gamma.Menu(300,70,
            [
                gamma.UITextMenuItem('No transition', actionListener=gamma.ActionListener(popScene)),
                gamma.UITextMenuItem('Black transition', actionListener=gamma.ActionListener(blackTransitionFirst)),
                gamma.UITextMenuItem('Fade transition', actionListener=gamma.ActionListener(fadeTransitionFirst)),
                gamma.UITextMenuItem('Wipe left transition', actionListener=gamma.ActionListener(wipeLeftTransitionFirst)),
                gamma.UITextMenuItem('Wipe right transition', actionListener=gamma.ActionListener(wipeRightTransitionFirst)),
                gamma.UITextMenuItem('Fly out left transition', actionListener=gamma.ActionListener(flyOutLeftTransitionFirst)),
                gamma.UITextMenuItem('Fly out right transition', actionListener=gamma.ActionListener(flyOutRightTransitionFirst)),
                gamma.UITextMenuItem('Fly in left transition', actionListener=gamma.ActionListener(flyInLeftTransitionFirst)),
                gamma.UITextMenuItem('Fly in right transition', actionListener=gamma.ActionListener(flyInRightTransitionFirst)),
                gamma.UITextMenuItem('Move left transition', actionListener=gamma.ActionListener(moveLeftTransitionFirst)),
                gamma.UITextMenuItem('Move right transition', actionListener=gamma.ActionListener(moveRightTransitionFirst))
            ]
        , spacing=25, entities=gamma.entityManager.getEntitiesByTag('player')), self)
    
    def draw(self):
        self.surface.fill(gamma.RED)
        gamma.drawText(self.surface, 'Second scene. Back to first scene using...', 25, 25, gamma.WHITE)
 
firstScene = FirstScene()
secondScene = SecondScene()

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Scenes and Transitions Example')
gamma.sceneManager.push(firstScene)
gamma.run()