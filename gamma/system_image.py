from .system import System
from .image import Image

class ImageSystem(System):

    def setRequirements(self):
        self.requiredComponents = ['imagegroups', 'position']
    
    def drawEntity(self, entity, scene):

        componentImageGroups = entity.getComponent('imagegroups')
        imageGroup = componentImageGroups.getCurrentImageGroup()
        if imageGroup is not None:
            image = imageGroup.getCurrentImage()
            if image is not None:
                componentPosition = entity.getComponent('position')
                scene.renderer.add(Image(
                    image,
                    componentPosition.x,
                    componentPosition.y,
                    componentPosition.w,
                    componentPosition.h,
                    componentPosition.angle == 270 and componentPosition.rotationStyle == 'leftRight',
                    False,
                    alpha=componentImageGroups.alpha
                ))
