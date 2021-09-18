from .gamma import resourceManager
from .renderable import Renderable
from .utils_draw import blit_alpha
from .colours import WHITE

class Text(Renderable):

    def __init__(self,

        # required parameters
        text, x, y,
        
        # optional parameters
        hAlign='left', vAlign='top',
        colour=WHITE,
        alpha=255,
        font=resourceManager.getFont('munro24'),
        underline=False

    ):

        super().__init__(x, y, hAlign, vAlign, colour, alpha)
        
        # set additional text object parameters 
        self._text = str(text)
        self.font = font
        self.underline = underline
        self._createSurface()

    def _createSurface(self):

        self.font.set_underline(self.underline)
        self.textSurface = self.font.render(self._text, True, self.colour)
        self.rect = self.textSurface.get_rect()
        self._align()

    def draw(self, surface, xOff=0, yOff=0, scale=1):

        x = self.rect.x * scale + xOff
        y = self.rect.y * scale + yOff
        blit_alpha(surface, self.textSurface, (x,y), self._alpha)        

    #  text property

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = str(value)
        self._createSurface()
