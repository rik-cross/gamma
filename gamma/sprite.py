import pygame
    
class Sprite:
    
    def __init__(self,
    
        texture,
        *additionalTextures,
        delay = 8,
        hFlip = False, vFlip = False,
        loop = True,
        afterAnimate = None
    
    ):
    
        # construct image list
        self.textureList = [texture]
        for i in additionalTextures:
            self.textureList.append(i)

        self.animationDelay = delay
        self.hFlip = hFlip
        self.vFlip = vFlip
        self.loop = loop
        self.afterAnimate = afterAnimate

        self.reset()

    def getCurrentTexture(self):

        if self.textureList == []:
            return None
        return self.textureList[self.textureIndex]

    def reset(self):

        self.animationTimer = 0
        self.textureIndex = 0

    def update(self):

        # increment the timer
        self.animationTimer += 1
        
        # if the timer gets too high...
        if self.animationTimer >= self.animationDelay:
            
            # reset the timer
            self.animationTimer = 0
            
            # increment the current texture
            self.textureIndex += 1
            
            # loop back to the first texture in the list
            # once the index gets too high
            if self.textureIndex > len(self.textureList) - 1:
                if self.loop:
                    self.textureIndex = 0
                else:
                    self.textureIndex = len(self.textureList) - 1
                # execute afterAnimate function, if one exists
                if self.afterAnimate is not None:
                    self.afterAnimate()
