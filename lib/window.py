from lib import debug, input, renderer, level
import pygame
import sys
from lib.renderer import *

WIN_RECT = (1200, 675)
DELTATIME = 0

def StartWindow(windowName = "FPS"):
    global WIN_RECT, GAME_WIN, WIN_CLOCK, WIN_FONT
    pygame.init()
    pygame.display.set_caption(windowName)
    GAME_WIN = pygame.display.set_mode(WIN_RECT, pygame.RESIZABLE)
    WIN_CLOCK = pygame.time.Clock()
    WIN_FONT = pygame.font.SysFont("Arial", 18)
    RenderInit(GAME_WIN)

def WindowLoop():
    global DELTATIME
    while True:
        if debug.DEBUG_ENABLED:
            t = pygame.time.get_ticks()
            DELTATIME = (t - debug.TICKSINCELASTFRAME) / 1000.0
            debug.TICKSINCELASTFRAME = t
        WIN_CLOCK.tick(75)
        GAME_WIN.fill((0,0,0))

        debug.Tick_Debug()
        level.Render(DELTATIME)
        pygame.display.flip()

        input.ProcessInput(pygame.key.get_pressed(), DELTATIME)

        if renderer.ROTATIONY > 6.28 or renderer.ROTATIONY < -6.28:
            renderer.ROTATIONY = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()