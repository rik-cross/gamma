from .image import Image
import pygame
from .gamma import resourceManager

def changeColour(image, colour):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(colour)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage
    
class ImageGroup:
    def __init__(self, image, *additionalImages, delay=8, loop=True):
        self.imageList = [image]
        for i in additionalImages:
            self.imageList.append(i)
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationDelay = delay
        self.loop = loop
        self.afterAnimate = None

    def getCurrentImage(self):
        if self.imageList == []:
            return None
        return self.imageList[self.imageIndex]

    def reset(self):
        self.animationTimer = 0
        self.imageIndex = 0

    def update(self):
        # increment the timer
        self.animationTimer += 1
        # if the timer gets too high...
        if self.animationTimer >= self.animationDelay:
            # reset the timer
            self.animationTimer = 0
            # increment the current image
            self.imageIndex += 1
            # loop back to the first image in the list
            # once the index gets too high
            if self.imageIndex > len(self.imageList) - 1:
                if self.loop:
                    self.imageIndex = 0
                else:
                    self.imageIndex = len(self.imageList) - 1
                if self.afterAnimate is not None:
                    self.afterAnimate()

    def draw(self, scene, x, y, w, h, alpha=255, hFlip=False, vFlip=False):
        image = self.imageList[self.imageIndex]
        scene.renderer.add(Image(
            resourceManager.getImage('cross'), x, y, w, h, hFlip, vFlip, 50#alpha
        ))