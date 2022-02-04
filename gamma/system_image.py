from .system import System
from .image import Image

class ImageSystem(System):

    def init(self):
        self.key = 'image'

    def setRequirements(self):
        self.requiredComponents = ['imagegroups', 'position']
    
    def drawEntity(self, entity, scene):

        # get the imagegroup to draw
        componentImageGroups = entity.getComponent('imagegroups')
        imageGroup = componentImageGroups.getCurrentImageGroup()

        # get the current image in the imagegroup
        if imageGroup is not None:
            image = imageGroup.getCurrentImage()


            # send the image to the renderer
            if image is not None:

                componentPosition = entity.getComponent('position')

                #
                # calculate angle and flip, based on rotation style
                #
                                
                v = imageGroup.vFlip
                h = imageGroup.hFlip
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
                    image,
                    componentPosition.x,
                    componentPosition.y,
                    componentPosition.w,
                    componentPosition.h,
                    # horizontal & vertical flip
                    h, v,
                    # rotation angle
                    a,
                    alpha=componentImageGroups.alpha,
                    hue = componentImageGroups.hue
                ), scene=False)
