import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from .managers.manager_sound import *
from .managers.manager_input import *
from .core.entity_factory import *
from .managers.manager_scene import *
from .managers.manager_system import *
from .managers.manager_entity import *

from .managers.manager_tile import TileManager
from .core.tile import Tile

from .systems.system_animation import *
from .systems.system_emote import *
from .systems.system_input import *
from .systems.system_particle import *
from .systems.system_physics import *
from .systems.system_text import *
from .systems.system_trauma import *
from .systems.system_trigger import *
from .systems.system_image import *
from .systems.system_collision import *
from .systems.system_inventory import *
from .systems.system_crafting import *
from .systems.system_battle import *

from .globals import ROOT_DIR

def quit():
    global sceneManager
    sceneManager.clear()

pygame.init()

clock = pygame.time.Clock()
windowSize = pygame.Rect(0,0,1200,800)
screen = pygame.display.set_mode((windowSize.w, windowSize.h))

from .core.assets import textureGamma

# create managers
sceneManager = SceneManager()
inputManager = InputManager()
soundManager = SoundManager()
tileManager = TileManager()
entityManager = EntityManager()

entityFactory = EntityFactory()

# add tiles
tileManager.addTile(Tile('none'))

# add core game systems
systemManager = SystemManager()
systemManager.addSystem(
    InputSystem(),
    PhysicsSystem(),
    CollisionSystem(),
    TraumaSystem(),
    TriggerSystem(),
    AnimationSystem(),
    ImageSystem(),
    EmoteSystem(),
    TextSystem(),
    ParticleSystem(),
    InventorySystem(),
    CraftingSystem(),
    Battleystem()
)

def init(size=(1200,800), caption='', icon=textureGamma):
    
    global screen
    global windowSize
    windowSize.w = size[0]
    windowSize.h = size[1]
    screen = pygame.display.set_mode((windowSize.w, windowSize.h))
    pygame.display.set_caption(caption)
    pygame.display.set_icon(icon)

def run(fps=60, showFPS=False):

    # game loop
    running = True
    while running:
    
        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        inputManager.processInput()
        soundManager.update()

        if sceneManager.isEmpty() and sceneManager.transition is None:
            running = False

        # get current scene
        sceneBeforeUpdate = sceneManager.getTopScene()
        
        # update
        sceneManager.update()

        # get new current scene after update
        sceneAfterUpdate = sceneManager.getTopScene()

        # only draw if the scene hasn't changed
        # (otherwise scene variables might not have been initialised)
        if sceneAfterUpdate is sceneBeforeUpdate:

            # draw
            screen.fill(BLACK)
            sceneManager.draw() 
            pygame.display.flip()

        # set maximum framerate
        clock.tick(fps)

        # show FPS as caption if required
        if showFPS:
            pygame.display.set_caption('FPS : ' + str(round(clock.get_fps(), 1)))

    # quit
    sceneManager.clear()
    pygame.quit()
