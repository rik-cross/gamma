import pygame
import os

from .soundmanager import *
from .inputmanager import *
from .scenemanager import *
from .resourcemanager import *

from .system import System

from .system_animation import *
from .system_camera import *
from .system_emote import *
from .system_input import *
from .system_particle import *
from .system_physics import *
from .system_text import *
from .system_trauma import *
from .system_trigger import *

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

# add core game systems
System.addSystem(AnimationSystem())
System.addSystem(EmoteSystem())
System.addSystem(InputSystem())
System.addSystem(PhysicsSystem())
System.addSystem(TextSystem())
System.addSystem(TraumaSystem())
System.addSystem(TriggerSystem())
System.addSystem(ParticleSystem())
System.addSystem(CameraSystem())

entityFactory = EntityFactory()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200,800))

def init(size, caption='', icon=resourceManager.getImage('default_icon')):
    global screen
    screen = pygame.display.set_mode(size)
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

        if sceneManager.isEmpty():
            running = False

        sceneManager.input()
        sceneManager.update()
        screen.fill((0,0,0))
        sceneManager.draw() 

        clock.tick(fps)

    # quit
    sceneManager.clear()
    pygame.quit()
