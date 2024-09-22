import pygame as pg

class Debug_Renderer():
    def __init__(self, app):
        self.app = app
        self.font = pg.font.SysFont('Arial', 18)

    def render(self):
        fps = round(self.app.clock.get_fps() * 100) / 100
        self.render_text((0, 0), fps, 18)

    def render_text(self, pos, text, fontsize, color = pg.Color("coral")):
        text_render = self.font.render(str(text), 0, color)
        self.app.win.blit(text_render, pos)
