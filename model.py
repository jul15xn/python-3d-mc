import numpy as np
import glm
import pygame as pg
import moderngl as mgl

class BaseModel:
    def __init__(self, app, vao_name, tex_id):
        self.app = app
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self):
        pass

    def get_model_matrix(self):
        m_model = glm.mat4()
        return m_model
    
    def render(self):
        self.update()
        self.vao.render()

class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0):
        super().__init__(app, vao_name, tex_id)    
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.app.camera.position)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        #texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['uv_texture_0'] = 0
        self.texture.use()
        #mvp
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)
        #lighting
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)