import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from .manager_resource import *
from .manager_sound import *
from .manager_input import *
from .entity_factory import *
from .manager_scene import *
from .manager_system import *
from .manager_entity import *

from .manager_tile import TileManager
from .tile import Tile

from .system_animation import *
from .system_camera import *
from .system_emote import *
from .system_input import *
from .system_particle import *
from .system_physics import *
from .system_text import *
from .system_trauma import *
from .system_trigger import *
from .system_image import *
from .system_collision import *
from .system_inventory import *
from .system_crafting import *
from .system_battle import *

# stores the path of this file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def quit():
    global sceneManager
    sceneManager.clear()

pygame.init()

clock = pygame.time.Clock()
windowSize = pygame.Rect(0,0,1200,800)
screen = pygame.display.set_mode((windowSize.w, windowSize.h))

# create managers
sceneManager = SceneManager()
inputManager = InputManager()
soundManager = SoundManager()
tileManager = TileManager()
resourceManager = ResourceManager()
entityManager = EntityManager()

entityFactory = EntityFactory()

# add font resources
resourceManager.addFont('munro18', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=18)
resourceManager.addFont('small', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=18)
resourceManager.addFont('munro24', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=24)
resourceManager.addFont('medium', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=24)
resourceManager.addFont('munro60', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=60)
resourceManager.addFont('large', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=60)

# add image resources
resourceManager.addImage('gamma', os.path.join(ROOT_DIR, 'images', 'gamma.png'))
resourceManager.addImage('tile_outline', os.path.join(ROOT_DIR, 'images', 'tile_outline.png'))
resourceManager.addImage('emote', os.path.join(ROOT_DIR, 'images', 'emote_box.png'))

# add tiles
tileManager.addTile(Tile('none'))

# add core game systems
systemManager = SystemManager()
systemManager.addSystem(
    CameraSystem(),
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

def init(size=(1200,800), caption='', icon=resourceManager.getImage('gamma')):
    
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
