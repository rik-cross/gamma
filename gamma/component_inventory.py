from .component import Component
from .colours import *
from .rectangle import Rectangle
from .text import Text
from .image import Image
from .gamma import resourceManager, inputManager, entityFactory, sceneManager
from math import floor

class InventoryComponent(Component):

    def __init__(self,
    
        # required parameters
        x, y,

        # optional parameters
        slots = 1,
        slot_size = 48,
        hidden = False,
        imagePadding = 6,

        slotColour = DARK_GREY,
        borderColour = LIGHT_GREY,
        selectedColour = WHITE,

        left = None,
        right = None,
        drop = None
    
    ):
        
        self.key = 'inventory'

        self.x = x
        self.y = y
        self.slots = slots
        self.slot_size = slot_size
        self.hidden = hidden
        self.imagePadding = imagePadding

        self.slotColour = slotColour
        self.borderColour = borderColour
        self.selectedColour = selectedColour

        # input
        self.left = left
        self.right = right
        self.drop = drop

        self.selected = 0

        self.items = [(None, 0) for i in range(self.slots)]
        self.images = [None for i in range(self.slots)]
    
    def addEntity(self, entityString, amount=1):

        # add to existing pile, if there is one
        for i in range(self.slots):
            if self.items[i][0] == entityString:
                self.items[i][1] += amount
                self.buildImages()
                return

        # else add to current slot
        if self.items[self.selected][0] is None:
            self.items[self.selected] = [entityString, amount]
            self.buildImages()

    def removeEntityFromSlot(self, slotNumber):
        if self.items[slotNumber] is not None:
            if self.items[slotNumber][1] > 0:
                self.items[slotNumber][1] = self.items[slotNumber][1] - 1
                if self.items[slotNumber][1] == 0:
                    self.items[slotNumber][0] = None
    
    def removeEntityByName(self, entityString, amount=1):
        for i in range(self.slots):
            if self.items[i][0] == entityString:
                if self.items[i][1] > 0:
                    self.items[i][1] = self.items[i][1] - amount
                    if self.items[i][1] <= 0:
                        self.items[i][0] = None
                    return

    def has(self, entityName, amount):
        total = 0
        for i in self.items:
            if i[0] is not None:
                if i[0] == entityName:
                    total += i[1]
        if total >= amount:
            return True
        return False

    def next(self):
        if self.selected < self.slots - 1:
            self.selected += 1
    
    def prev(self):
        if self.selected > 0:
            self.selected -= 1

    def dropItem(self):
        # return None if there's no item to drop
        if self.items[self.selected][0] is None or self.items[self.selected][1] == 0:
            return None
        # return the entity dropped
        entityString = self.items[self.selected][0]
        entity = entityFactory.create(entityString, 0, 0)
        # remove one from the inventory
        self.removeEntityFromSlot(self.selected)
        return entity

    def buildImages(self):
        self.images = []
        # for all filled slots
        for i in range(self.slots):
            if self.items[i][0] is not None:
                # create entity
                ent = entityFactory.create(self.items[i][0], 0, 0)
                igs = ent.getComponent('sprites')
                if len(igs.animationList) > 0:
                    # get first key
                    key = list(igs.animationList.keys())[0]
                    ig = igs.animationList[key]
                    img = ig.imageList[0]
                    self.images.append(img)
                else:
                    self.images.append(None)
            else:
                self.images.append(None)

    def draw(self, scene):
        
        # draw slots
        for i in range(self.slots):

            # calculate x position
            x = self.x + (self.slot_size * i)
            
            # draw border
            scene.renderer.add(
                Rectangle(
                    x, self.y,
                    self.slot_size, self.slot_size,
                    colour=self.selectedColour if i == self.selected else self.borderColour
                )
            )
            
            # draw slot
            scene.renderer.add(
                Rectangle(
                    x+2, self.y+2,
                    self.slot_size-4, self.slot_size-4,
                    colour=self.slotColour
                )
            )

            # draw item, if one exists
            for i in range(len(self.items)):
                if self.items[i][0] is not None:
                    img = self.images[i]

                    imageRect = img.get_rect()

                    # resize the image to be 18x18 max
                    w = imageRect.w
                    h = imageRect.h
                    percentageResize = 0
                    # resize based on width if greater
                    if w >= h:
                        percentageResize = w/(self.slot_size-self.imagePadding*2)
                        w = (self.slot_size-self.imagePadding*2)
                        h = floor(h / percentageResize)
                    # resize based on height if greater
                    else:
                        percentageResize = h/(self.slot_size-self.imagePadding*2)
                        h = (self.slot_size-self.imagePadding*2)
                        w = floor(w / percentageResize)

                    scene.renderer.add(
                        Image(
                            img,
                            self.x + i*self.slot_size + self.slot_size//2,
                            self.y + self.slot_size//2,
                            w=w, h=h,
                            hAlign='center', vAlign='middle'
                        )
                    )

            # draw amount, if > 0
            for i in range(len(self.items)):
                if self.items[i][1] > 0:
                    scene.renderer.add(
                        Text(
                            self.items[i][1],
                            self.x + i*self.slot_size + self.slot_size - 3,
                            self.y + self.slot_size - 1,
                            hAlign='right', vAlign='bottom',
                            colour=WHITE,
                            font=resourceManager.getFont('munro18')
                        )
                    )
        