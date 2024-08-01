import gamma

#
# create a player entity to control the menu
#

playerEntity = gamma.Entity()
playerEntity.addComponent(gamma.InputComponent(up=gamma.keys.up, down=gamma.keys.down, left=gamma.keys.left, right=gamma.keys.right, b1=gamma.keys.enter))
# optionally store the entity in the entityManager
playerEntity.getComponent(gamma.TagsComponent).add('player')
gamma.entityManager.addEntity(playerEntity)

#
# create some functions to attach to the menu buttons
#

def changeToSecondScene(transitionType=gamma.TransitionNone, easingFunction=None):
    gamma.sceneManager.setTransition(transitionType([firstScene],[secondScene], easingFunction=easingFunction))

def changeToFirstScene(transitionType=gamma.TransitionNone, easingFunction=None):
    gamma.sceneManager.setTransition(transitionType([secondScene],[], easingFunction=easingFunction))

#
# create scenes
#

class FirstScene(gamma.Scene):

    def init(self):

        self.background = gamma.BLUE

        self.setMenu(gamma.Menu(300,70,
            [
                gamma.UITextMenuItem('No transition', actionListener=gamma.ActionListener(changeToSecondScene)),
                gamma.UITextMenuItem('Black transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionBlack)),
                gamma.UITextMenuItem('Wipe left transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionWipeLeft)),
                gamma.UITextMenuItem('Wipe right transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionWipeRight)),
                gamma.UITextMenuItem('Fly out left transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionFlyOutLeft)),
                gamma.UITextMenuItem('Fly out right transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionFlyOutRight)),
                gamma.UITextMenuItem('Fly in left transition (with bounce)', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionFlyInLeft, gamma.easeOutBounce)),
                gamma.UITextMenuItem('Fly in right transition (with bounce)', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionFlyInRight, gamma.easeOutBounce)),
                gamma.UITextMenuItem('Move left transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionMoveLeft)),
                gamma.UITextMenuItem('Move right transition', actionListener=gamma.ActionListener(changeToSecondScene, gamma.TransitionMoveRight)),
                gamma.UITextMenuItem('Quit', actionListener=gamma.ActionListener(gamma.quit))
            ]
        , spacing=25, entities=gamma.entityManager.getEntitiesByTag('player')), self)

    def draw(self):
        self.renderer.add(gamma.Text('First scene. Move to second scene using...', 25, 25, colour=gamma.WHITE))

class SecondScene(gamma.Scene):

    def init(self):

        self.background = gamma.RED

        self.setMenu(gamma.Menu(300,70,
            [
                gamma.UITextMenuItem('No transition', actionListener=gamma.ActionListener(changeToFirstScene)),
                gamma.UITextMenuItem('Black transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionBlack)),
                gamma.UITextMenuItem('Wipe left transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionWipeLeft)),
                gamma.UITextMenuItem('Wipe right transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionWipeRight)),
                gamma.UITextMenuItem('Fly out left transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionFlyOutLeft)),
                gamma.UITextMenuItem('Fly out right transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionFlyOutRight)),
                gamma.UITextMenuItem('Fly in left transition (with bounce)', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionFlyInLeft, gamma.easeOutBounce)),
                gamma.UITextMenuItem('Fly in right transition (with bounce)', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionFlyInRight, gamma.easeOutBounce)),
                gamma.UITextMenuItem('Move left transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionMoveLeft)),
                gamma.UITextMenuItem('Move right transition', actionListener=gamma.ActionListener(changeToFirstScene, gamma.TransitionMoveRight)),
                gamma.UITextMenuItem('Quit', actionListener=gamma.ActionListener(gamma.quit))
            ]
        , spacing=25, entities=gamma.entityManager.getEntitiesByTag('player')), self)
    
    def draw(self):
        self.renderer.add(gamma.Text('Second scene. Back to first scene using...', 25, 25, colour=gamma.WHITE))

firstScene = FirstScene()
secondScene = SecondScene()

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Scenes and Transitions Example')
gamma.sceneManager.push(firstScene)
gamma.run()