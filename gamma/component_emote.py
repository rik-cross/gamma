import pygame

from .component import Component
from .colours import *

class EmoteComponent(Component):

    def __init__(self, image, timed=True, timer=200, backgroundColour=WHITE):
        self.key = 'emote'
        self.image = image
        self.backgroundColour = backgroundColour
        self.timed = timed
        self.timer = timer
        self.bottomMargin = 10
        self.imagePadding = 10
        self.pointerWidth = 10
        self.pointerHeight = 10
        self.destroy = False
    
    def update(self):
        # decrement timer
        if self.timed:
            self.timer -= 1
            # destroy if timer reaches 0
            if self.timer <= 0:
                self.destroy = True

    def draw(self, screen, middleX, y, zoom):
        # get image dimensions
        imageRect = self.image.get_rect()
        w = int(imageRect.w * zoom)
        h = int(imageRect.h * zoom)

        # calculate pointer position
        triangleLeft = middleX - (self.pointerWidth * zoom)
        triangleRight = middleX + (self.pointerWidth * zoom)
        triangleTop = y - (self.bottomMargin * zoom) - (self.pointerHeight * zoom) - 1
        triangleBottom = y - (self.bottomMargin * zoom)

        # calculate rectangle position
        rectX = int(middleX - w/2 - (self.imagePadding * zoom))
        rectY = int(y - h - (self.bottomMargin * zoom) - (2 * self.imagePadding * zoom) - (self.pointerHeight * zoom))
        bgRect = pygame.rect.Rect(rectX, rectY, w + (self.imagePadding * 2 * zoom), h + (self.imagePadding * 2 * zoom))
        bgOutineRect = pygame.rect.Rect(rectX-zoom, rectY-zoom, w + (self.imagePadding * 2 * zoom) + (2 * zoom), h + (self.imagePadding * 2 * zoom) + (2 * zoom))
        
        # calculate image position
        imageX = int(middleX - w/2)
        imageY = int(y - h - (self.bottomMargin * zoom) - (self.imagePadding * zoom) - (self.pointerHeight * zoom))
        
        # draw outine
        # draw pointer outine
        pygame.draw.polygon(screen, BLACK, ((triangleLeft - zoom, triangleTop), (triangleRight + zoom, triangleTop), (middleX, triangleBottom + zoom)))
        # draw rectangle outine
        pygame.draw.rect(screen, BLACK, bgOutineRect)

        # draw pointer
        pygame.draw.polygon(screen, self.backgroundColour, ((triangleLeft, triangleTop), (triangleRight, triangleTop), (middleX , triangleBottom)))
        # draw rectangle
        pygame.draw.rect(screen, self.backgroundColour, bgRect)
        # draw emote image
        screen.blit(pygame.transform.scale(self.image, (w, h)), (imageX, imageY))
