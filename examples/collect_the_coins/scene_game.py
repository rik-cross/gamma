import gamma
from component_score import ScoreComponent
from scene_game_over import GameOverScene
from input_context_player import playerInputContext
from assets import texturePlayer

class GameScene(gamma.Scene):

    def init(self):

        self.background = gamma.CORNFLOWER_BLUE

        # add a camera to the scene
        # the same size as the screen, but with a 10px border
        self.cameras.append(
            gamma.Camera(10, 10, gamma.windowSize.w-20, gamma.windowSize.h-20, bgColour=gamma.DARK_GREY)
        )

        # create a player entity
        player = gamma.Entity(
            
            # adding a tag to the player with help determine collision befaviour
            gamma.TagsComponent('player'),
            
            # player is centered at (0,0)
            gamma.PositionComponent(0, 0, 45, 51, z=4, xAnchor='center', yAnchor='middle'),
            
            # add an Sprite (tagged as 'default') to the player, consisting of a single image (i.e. not an animation)
            gamma.SpritesComponent('default', gamma.Sprite(texturePlayer)),
            
            # player uses WASD to move
            # the effect of pressing WASD is described in the 'playerInputContext' function
            gamma.InputComponent(gamma.keys.w, gamma.keys.s, gamma.keys.a, gamma.keys.d, inputContext=playerInputContext),
            
            # player has a collider, which allows it to collect coins
            # collider is 5 pixels smaller than the player on all sides
            gamma.ColliderComponent(5, 5, 35, 41),
            
            # add the custom score component
            ScoreComponent()
        )
        
        # add the entity to the scene
        self.addEntity(player)

        # create a timer, and set the initial value
        self.timer = 15 - (self.frame // 60)
    
    def onEnter(self):
        gamma.soundManager.playMusicFade('dawn')

    def update(self):

        # esc to quit
        if gamma.inputManager.isPressed(gamma.keys.esc):
            gamma.sceneManager.pop()
        
        # update the game timer
        self.timer = 15 - (self.frame // 60)
        # end the game when the timer reaches 0
        if self.timer == 0:
            # show gameOver scene as overlay
            gamma.sceneManager.push(GameOverScene(entities=self.getEntitiesByTag('player')))

        # create score text
        self.scoreText = gamma.Text(
            self.getEntitiesByTag('player')[0].getComponent(ScoreComponent).score,
            25, 15,
            font=gamma.fontDefaultLarge
        )

        # create timer text
        self.timerText = gamma.Text(
            self.timer,
            580, 15,
            hAlign='right',
            font=gamma.fontDefaultLarge
        )

    def draw(self):

        # display the player score
        self.renderer.add(self.scoreText)
        
        # display the timer
        self.renderer.add(self.timerText)
