# import and initialise gamma
import gamma
import os

gamma.init((600, 400), caption='Gamma // Renderable Objects Example')

# add a font
gamma.resourceManager.addFont('large', os.path.join('..', 'gamma', 'fonts', 'munro.ttf'), size=64)

# create a main scene class
class RenderableScene(gamma.Scene):
    
    def init(self):

        # title text example, using all parameters
        self.titleText = gamma.Text(
            'Title text',
            gamma.windowSize.w/2,
            100,
            colour=gamma.YELLOW,
            alpha=255,
            hAlign='center',
            vAlign='middle',
            font=gamma.resourceManager.getFont('large'),
            underline=True
        )

        # text showing the frame number 
        self.frameText = gamma.Text(
            self.frame, 0, gamma.windowSize.h,
            vAlign='bottom',
            colour=gamma.RED
        )

        # circle
        self.circle = gamma.Circle(
            gamma.windowSize.w/2, 100, 75,
            hAlign='center',
            vAlign='middle',
            colour=gamma.GREEN,
            alpha=100
        )

        # rectangle
        self.rectangle = gamma.Rectangle(
            gamma.windowSize.w//2,
            200,
            200,
            100,
            hAlign='center',
            colour=gamma.DARK_GREY
        )

        self.image = gamma.Image(
            gamma.resourceManager.getImage('gamma_icon'),
            gamma.windowSize.w, 0,
            w=40, h=40,
            hAlign='right'
        )

    def update(self):

        self.frameText.text = self.frame
        self.circle.radius = min(75, self.frame)
        self.image.alpha = min(255, self.frame)
        if self.frame == 120:
            self.image.flipX = True

    def draw(self):
        
        gamma.Text('Hello world!', 0, 0).draw(self.surface)
        self.titleText.draw(self.surface)
        self.frameText.draw(self.surface)
        self.circle.draw(self.surface)
        self.rectangle.draw(self.surface)
        self.image.draw(self.surface)
        
# create a scene instance
scene = RenderableScene()

# add scene to the gamma and start
gamma.sceneManager.push(scene)
gamma.run()