import pygame

def changeColour(image, colour):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(colour)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage
    
class ImageGroup:
    def __init__(self, image, *additionalImages, delay=8):
        self.imageList = [image]
        for i in additionalImages:
            self.imageList.append(i)
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationDelay = delay
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
                self.imageIndex = 0
    def draw(self, screen, x, y, flipX, flipY, zoomLevel, alpha, hue=None):
        image = self.imageList[self.imageIndex]
        if hue is not None:
            colour = pygame.Color(0)
            colour.hsla = (hue, 100, 50, 100)
            image = changeColour(image,colour)
        image.set_alpha(alpha)
        newWidth = int(image.get_rect().w * zoomLevel)
        newHeight = int(image.get_rect().h * zoomLevel)
        screen.blit(pygame.transform.scale(pygame.transform.flip(image, flipX, flipY), (newWidth, newHeight)), (x, y))