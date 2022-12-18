from ..core.system import System
from ..renderables.image import Image

class ImageSystem(System):

    def init(self):
        self.key = 'image'

    def setRequirements(self):
        self.requiredComponents = ['sprites', 'position']
    
    def drawEntity(self, entity, scene):

        # get the Sprite to draw
        componentSprites = entity.getComponent('sprites')
        sprite = componentSprites.getCurrentSprite()

        # get the current image in the Sprite
        if sprite is not None:

            texture = sprite.getCurrentTexture()

            # send the image to the renderer
            if texture is not None:

                componentPosition = entity.getComponent('position')

                #
                # calculate angle and flip, based on rotation style
                #
                                
                v = sprite.vFlip
                h = sprite.hFlip
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
                    componentPosition.x - sprite.xOffset,
                    componentPosition.y - sprite.yOffset,
                    texture.get_rect().w,
                    texture.get_rect().h,
                    # horizontal & vertical flip
                    h, v,
                    # rotation angle
                    a,
                    alpha=componentSprites.alpha,
                    hue=componentSprites.hue
                ), scene=False)
