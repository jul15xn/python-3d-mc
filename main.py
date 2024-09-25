import settings as sts
import moderngl as mgl
import pygame as pg
import sys
from shader_program import ShaderProgram
from scene import Scene
from player import Player
from textures import Textures
from console import Console
from noise import *

class VoxelEngine:
    def __init__(self, seed):
        sts.SEED = seed

        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, sts.MAJOR_VER)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, sts.MINOR_VER)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, sts.DEPTH_SIZE)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, sts.NUM_SAMPLES)

        pg.display.set_mode(sts.WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        pg.display.set_caption(str(sts.SEED))
        seed_init()
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self):
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        self.player.update()
        self.shader_program.update()
        self.scene.update()

        self.delta_time = self.clock.tick(sts.FPS_LIMIT)
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{sts.SELECTED_BLOCK} {self.clock.get_fps() :.0f}')

    def render(self):
        self.ctx.clear(color=sts.BG_COLOR)
        self.scene.render()
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            self.player.handle_event(event=event)

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    console = Console()
    output = console.run()
    if output['choise'] == "singleplayer":
        app = VoxelEngine(output['seed'])
        app.run()
