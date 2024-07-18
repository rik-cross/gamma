

import pygame

from .managers.manager_resource import *
from .managers.manager_sound import *
from .managers.manager_input import *
from .core.entity_factory import *
from .managers.manager_scene import *
from .managers.manager_system import *
from .managers.manager_entity import *

from .managers.manager_tile import TileManager
from .core.tile import Tile

from .systems.system_animation import *
from .systems.system_camera import *
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

from gamma import ROOT_DIR

class Game:

    def __init__(self, size=(1200,800), caption='Gamma', icon=None):

        pygame.init()

        self.size = size
        
        self.clock = pygame.time.Clock()
        #self.windowSize = pygame.Rect(0,0,1200,800)
        self.screen = pygame.display.set_mode(self.size)     

        # create managers
        self.sceneManager = SceneManager()
        self.inputManager = InputManager()
        self.soundManager = SoundManager()
        self.tileManager = TileManager()
        self.resourceManager = ResourceManager()
        self.entityManager = EntityManager()

        self.entityFactory = EntityFactory()

        # add font resources
        self.resourceManager.addFont('munro18', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=18)
        self.resourceManager.addFont('small', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=18)
        self.resourceManager.addFont('munro24', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=24)
        self.resourceManager.addFont('medium', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=24)
        self.resourceManager.addFont('munro60', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=60)
        self.resourceManager.addFont('large', os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=60)

        # add image resources
        self.resourceManager.addTexture('gamma', os.path.join(ROOT_DIR, 'images', 'gamma.png'))
        self.resourceManager.addTexture('tile_outline', os.path.join(ROOT_DIR, 'images', 'tile_outline.png'))
        self.resourceManager.addTexture('emote', os.path.join(ROOT_DIR, 'images', 'emote_box.png'))

        # add tiles
        self.tileManager.addTile(Tile('none'))

        # add core game systems
        self.systemManager = SystemManager()
        self.systemManager.addSystem(
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

        pygame.display.set_caption(caption)

        if icon == None:
            icon = self.resourceManager.getTexture('gamma')
        pygame.display.set_icon(icon)

    def run(self, fps=60, showFPS=False):

        # game loop
        running = True
        while running:
        
            # check for quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.inputManager.processInput()
            self.soundManager.update()

            if self.sceneManager.isEmpty() and self.sceneManager.transition is None:
                running = False

            # get current scene
            sceneBeforeUpdate = self.sceneManager.getTopScene()
            
            # update
            self.sceneManager.update()

            # get new current scene after update
            sceneAfterUpdate = self.sceneManager.getTopScene()

            # only draw if the scene hasn't changed
            # (otherwise scene variables might not have been initialised)
            if sceneAfterUpdate is sceneBeforeUpdate:

                # draw
                self.screen.fill(BLACK)
                self.sceneManager.draw() 
                pygame.display.flip()

            # set maximum framerate
            self.clock.tick(fps)

            # show FPS as caption if required
            if showFPS:
                pygame.display.set_caption('FPS : ' + str(round(self.clock.get_fps(), 1)))

        # quit
        self.sceneManager.clear()
        pygame.quit()

    def quit(self):

        self.sceneManager.clear()
