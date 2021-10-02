from .component import Component
from .colours import *
from .rectangle import Rectangle
from .text import Text
from .image import Image
from .gamma import resourceManager, inputManager, entityFactory, sceneManager
from math import floor

class CraftingComponent(Component):

    def __init__(self,
    
        # required parameters
        x, y,
        entity,
        scene,

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
        craft = None
    
    ):
        
        self.key = 'crafting'

        self.x = x
        self.y = y
        self.entity = entity
        self.scene = scene
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
        self.craft = craft

        self.selected = 0

        self.items = []
        self.images = []
    
    def addRecipe(self, recipe):

        if len(self.items) < self.slots:
            self.items.append(recipe)

        self.buildImages()

    def removeRecipe(self, recipeString):
        for i in self.items:
            if i.output == recipeString:
                self.items.remove(i)

    def update(self):
        
        # controls

        # left
        if inputManager.isPressed(self.left) and self.selected > 0:
            self.selected -= 1
        # right
        if inputManager.isPressed(self.right) and self.selected < len(self.items) - 1:
            self.selected += 1
        # drop
        if inputManager.isPressed(self.craft):
            
            canCraft = True
            craftRecipe = self.items[self.selected]
            itemToCraft = craftRecipe.output
            inv = self.entity.getComponent('inventory')
            
            for inp in craftRecipe.inputs:
                if not inv.has(inp[0], inp[1]):
                    canCraft = False

            if canCraft:
                for inp in craftRecipe.inputs:
                    inv.removeEntityByName(inp[0], inp[1])
            
                inv.addEntity(itemToCraft, 1)

    def buildImages(self):

        self.images = {}
        
        # for all filled slots
        for i in range(len(self.items)):
            if self.items[i] is not None:

                # create output entity
                ent = entityFactory.create(self.items[i].output, 0, 0)
                igs = ent.getComponent('imagegroups')
                if len(igs.animationList) > 0:
                    # get first key
                    key = list(igs.animationList.keys())[0]
                    ig = igs.animationList[key]
                    img = ig.imageList[0]
                    self.images[self.items[i].output] = img
                
                # create input entities
                for inp in self.items[i].inputs:
                    #print(inp[0], inp[1])
                    ent = entityFactory.create(inp[0], 0, 0)
                    igs = ent.getComponent('imagegroups')
                    if len(igs.animationList) > 0:
                        # get first key
                        key = list(igs.animationList.keys())[0]
                        ig = igs.animationList[key]
                        img = ig.imageList[0]
                        self.images[inp[0]] = img

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
        
            # draw output item
            for i in range(len(self.items)):

                img = self.images[self.items[i].output]
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

        # draw requirements for selected entity
        for x in range(len(self.items[self.selected].inputs)):

            inp = self.items[self.selected].inputs[x]

            img = self.images[inp[0]]
            imageRect = img.get_rect()

            # resize the image to be 18x18 max
            w = imageRect.w
            h = imageRect.h
            percentageResize = 0
            # resize based on width if greater
            if w >= h:
                percentageResize = w/((self.slot_size)-self.imagePadding*2)
                w = ((self.slot_size)-self.imagePadding*2)
                h = floor(h / percentageResize)
            # resize based on height if greater
            else:
                percentageResize = h/((self.slot_size)-self.imagePadding*2)
                h = ((self.slot_size)-self.imagePadding*2)
                w = floor(w / percentageResize)

            if self.entity.getComponent('inventory').has(inp[0], inp[1]):
                aa=255
            else:
                aa=100

            scene.renderer.add(
                Image(
                    img,
                    self.x+(w*x),self.y+self.slot_size+5,w/2,h/2,
                    alpha=aa
                )
            )
            scene.renderer.add(
                Text(
                    inp[1], self.x+w/2+2+(w*x), self.y+self.slot_size+h/2+5,
                    font=resourceManager.getFont('munro18'),
                    vAlign='bottom', alpha=aa
                )
            )        
