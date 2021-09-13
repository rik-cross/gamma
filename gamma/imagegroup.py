import pygame
    
class ImageGroup:
    
    def __init__(self,
    
        image,
        *additionalImages,
        delay = 8,
        loop = True,
        afterAnimate = None
    
    ):
    
        # construct image list
        self.imageList = [image]
        for i in additionalImages:
            self.imageList.append(i)

        self.animationDelay = delay
        self.loop = loop
        self.afterAnimate = afterAnimate

        self.reset()

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
                # execute afterAnimate function, if one exists
                if self.afterAnimate is not None:
                    self.afterAnimate()
