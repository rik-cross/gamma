import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from .manager_sound import *
from .manager_input import *
from .manager_scene import *
from .manager_resource import *
from .manager_system import *

from .system_animation import *
from .system_camera import *
from .system_emote import *
from .system_input import *
from .system_particle import *
from .system_physics import *
from .system_text import *
from .system_trauma import *
from .system_trigger import *

from .manager_entity import *
from .entity_factory import *

from .world import *

# stores the path of this file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

sceneManager = SceneManager()
inputManager = InputManager()
soundManager = SoundManager()
resourceManager = ResourceManager()
resourceManager.addFont('munro24', ROOT_DIR + '/fonts/munro.ttf')
resourceManager.addImage('default_icon', ROOT_DIR + '/images/icon.png')
resourceManager.addImage('tile_outline', ROOT_DIR + '/images/tile_outline.png')
resourceManager.addImage('cross', ROOT_DIR + '/images/cross.png')

# add core game systems
systemManager = SystemManager()
systemManager.addSystem(
    AnimationSystem(),
    EmoteSystem(),
    InputSystem(),
    PhysicsSystem(),
    TextSystem(),
    TraumaSystem(),
    TriggerSystem(),
    ParticleSystem(),
    CameraSystem()
)

entityManager = EntityManager()
entityFactory = EntityFactory()

clock = pygame.time.Clock()

windowSize = pygame.Rect(0,0,1200,800)
screen = pygame.display.set_mode((windowSize.w, windowSize.h))

def init(size=(1200,800), caption='', icon=resourceManager.getImage('default_icon')):
    global screen
    global windowSize
    windowSize.w = size[0]
    windowSize.h = size[1]
    screen = pygame.display.set_mode((windowSize.w, windowSize.h))
    pygame.display.set_caption(caption)
    pygame.display.set_icon(icon)

def run(fps=60):
    running = True
    while running:
    # game loop

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        inputManager.processInput()
        soundManager.update()

        if sceneManager.isEmpty() and sceneManager.transition is None:
            running = False

        # input
        sceneManager.input()
        # update
        sceneManager.update()
        # draw
        screen.fill((0,0,0))
        sceneManager.draw() 
        pygame.display.flip()

        # set maximum framerate
        clock.tick(fps)

    # quit
    sceneManager.clear()
    pygame.quit()
