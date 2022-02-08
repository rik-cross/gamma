from .system import System
from .image import Image

class ImageSystem(System):

    def init(self):
        self.key = 'image'

    def setRequirements(self):
        self.requiredComponents = ['sprites', 'position']
    
    def drawEntity(self, entity, scene):

        # get the Sprite to draw
        componentSprites = entity.getComponent('sprites')
        Sprite = componentSprites.getCurrentSprite()

        # get the current image in the Sprite
        if Sprite is not None:
            texture = Sprite.getCurrentTexture()


            # send the image to the renderer
            if texture is not None:

                componentPosition = entity.getComponent('position')

                #
                # calculate angle and flip, based on rotation style
                #
                                
                v = Sprite.vFlip
                h = Sprite.hFlip
                a = 0

                #if componentPosition.rotationStyle == 'none':
                #    pass
                #elif componentPosition.rotationStyle == 'allAround':
                #    a = componentPosition.angle * -1
                #elif componentPosition.rotationStyle == 'leftRight':
                #    if 180 <= componentPosition.angle % 360 <= 360:
                #        h = not h
                #elif componentPosition.rotationStyle == 'upDown':
                #    if 91 <= componentPosition.angle % 360 <= 270:
                #        v = not v

                scene.renderer.add(Image(
                    texture,
                    componentPosition.x,
                    componentPosition.y,
                    componentPosition.w,
                    componentPosition.h,
                    # horizontal & vertical flip
                    h, v,
                    # rotation angle
                    a,
                    alpha=componentSprites.alpha,
                    hue=componentSprites.hue
                ), scene=False)
