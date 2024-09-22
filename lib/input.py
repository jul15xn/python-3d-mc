from lib import renderer
import pygame

def ProcessInput(input, dt):
    if input[pygame.K_RIGHT]:
        renderer.ROTATIONY += 2 * dt
    if input[pygame.K_LEFT]:
        renderer.ROTATIONY -= 2 * dt