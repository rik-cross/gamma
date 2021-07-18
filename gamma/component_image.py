import pygame

def changeColour(image, colour):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(colour)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage
    
class Image:
    def __init__(self, image):
        self.image = image
    def update(self):
        pass
    def draw(self, screen, x, y, flipX, flipY, zoomLevel, alpha, hue=None):
        image = self.image
        if hue is not None:
            colour = pygame.Color(0)
            colour.hsla = (hue, 100, 50, 100)
            image = changeColour(image,colour)
        image.set_alpha(alpha)
        newWidth = int(image.get_rect().w * zoomLevel)
        newHeight = int(image.get_rect().h * zoomLevel)
        screen.blit(pygame.transform.scale(pygame.transform.flip(image, flipX, flipY), (newWidth, newHeight)), (x, y))