import pygame as pg

class Debug_Renderer():
    def __init__(self, app):
        self.app = app
        self.font = pg.font.SysFont('Arial', 18)

    def render(self):
        fps = round(self.app.clock.get_fps() * 100) / 100
        self.render_text(str(fps))

    def render_text(self, text, position=(50, 50), color=(255, 255, 255)):
        text_surface = self.app.font.render(text, True, color)
        text_surface = pg.transform.flip(text_surface, False, True)
        text_data = pg.image.tostring(text_surface, "RGBA", True)
        text_size = text_surface.get_size()
        text_texture = self.app.ctx.texture(text_size, 4, text_data)
        text_texture.use()