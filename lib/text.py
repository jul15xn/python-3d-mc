from lib import window
import pygame

def draw_text(pos, text, fontsize, color = pygame.Color("coral")):
    text_render = window.WIN_FONT.render(str(text), 0, color)
    window.GAME_WIN.blit(text_render, pos)