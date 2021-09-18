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

                scene.renderer.add(Image(
                    image,
                    componentPosition.x,
                    componentPosition.y,
                    componentPosition.w,
                    componentPosition.h,
                    # draw the image facing in the correct direction
                    componentPosition.angle == 270 and componentPosition.rotationStyle == 'leftRight',
                    False,
                    alpha=componentImageGroups.alpha
                ), scene=False)
