import moderngl as mgl
import numpy as np
import glm


class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        # resolution
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        # depth texture
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


#class MovingCube(Cube):
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        
    #def update(self):
        #self.m_model = self.get_model_matrix()
        #super().update()

class Cat(ExtendedBaseModel):
    def __init__(self, app, vao_name='cat', tex_id='cat',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(2, 2, 2)):
        adjusted_y = scale[1] * 0.8  # คำนวณตำแหน่ง Y ใหม่จาก scale
        pos = (pos[0], adjusted_y, pos[2])  # ปรับตำแหน่งแกน Y
        
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Coral(ExtendedBaseModel):
    def __init__(self, app, vao_name='coral', tex_id='coral',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        adjusted_y = scale[1] * -2.5  # คำนวณตำแหน่ง Y ใหม่จาก scale
        pos = (pos[0], adjusted_y, pos[2])  # ปรับตำแหน่งแกน Y
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        

class Kelp(ExtendedBaseModel):
    def __init__(self, app, vao_name='kelp', tex_id='kelp',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Greenkelp(ExtendedBaseModel):
    def __init__(self, app, vao_name='greenkelp', tex_id='greenkelp',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(3, 3, 3)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        

class Greenkelp1(ExtendedBaseModel):
    def __init__(self, app, vao_name='greenkelp', tex_id='greenkelp',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(1.5, 1.5, 1.5)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
                       
class Clam(ExtendedBaseModel):
    def __init__(self, app, vao_name='clam', tex_id='clam',
                 pos=(0, 1, 0), rot=(0, 180, 0), scale=(0.1, 0.1, 0.1)):
        adjusted_y = scale[1] * -2.5  # คำนวณตำแหน่ง Y ใหม่จาก scale
        pos = (pos[0], adjusted_y, pos[2])  # ปรับตำแหน่งแกน Y
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Pushilin(ExtendedBaseModel):
    def __init__(self, app, vao_name='pushilin', tex_id='pushilin',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(3.5, 3.5, 3.5)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Ice(ExtendedBaseModel):
    def __init__(self, app, vao_name='ice', tex_id='ice',
                 pos=(0, 1, 0), rot=(0, 0, 0), scale=(0.7, 0.7, 0.7)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Octopus(ExtendedBaseModel):
    def __init__(self, app, vao_name='octopus', tex_id='octopus',
                 pos=(2, 1, -5), rot=(0, 210, 0), scale=(0.1, 0.1, 0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Squid(ExtendedBaseModel):
    def __init__(self, app, vao_name='squid', tex_id='squid',
                 pos=(2, 1, -5), rot=(0, 210, 0), scale=(0.5, 0.5, 0.5)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        
        
class Salmon(ExtendedBaseModel):
    def __init__(self, app, vao_name='salmon', tex_id='salmon',
                 pos=(2, 1, -5), rot=(0, 0, 0), scale=(0.09, 0.09, 0.09)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Goldfish(ExtendedBaseModel):
    def __init__(self, app, vao_name='goldfish', tex_id='goldfish',
                 pos=(2, 1, -5), rot=(0, 0, 0), scale=(0.05, 0.05, 0.05)):
        super().__init__(app, vao_name, tex_id, glm.vec3(pos), rot, scale)  # เปลี่ยน pos เป็น glm.vec3
        
class Shark(ExtendedBaseModel):
    def __init__(self, app, vao_name='shark', tex_id='shark',
                 pos=(2, 1, -5), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Whale(ExtendedBaseModel):
    def __init__(self, app, vao_name='whale', tex_id='whale',
                 pos=(2, 1, -5), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Hibiscus(ExtendedBaseModel):
    def __init__(self, app, vao_name='hibiscus', tex_id='hibiscus',
                 pos=(0, 1, 0), rot=(10, 90, 0), scale=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)        

class Crayfish(ExtendedBaseModel):
    def __init__(self, app, vao_name='crayfish', tex_id='crayfish',
                 pos=(0, 1, 0), rot=(10, 90, 0), scale=(0.8, 0.8, 0.8)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)        

class Sand(ExtendedBaseModel):
    def __init__(self, app, vao_name='sand', tex_id='sand',
                 pos=(0, 1, 0), rot=(10, 90, 0), scale=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)   
        
class Turtle(ExtendedBaseModel):
    def __init__(self, app, vao_name='turtle', tex_id='turtle',
                 pos=(0, 1, 0), rot=(10, 90, 0), scale=(0.1, 0.1, 0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)   
 
class SkyBox(BaseModel):
    def __init__(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))


class AdvancedSkyBox(BaseModel):
    def __init__(self, app, vao_name='advanced_skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        m_view = glm.mat4(glm.mat3(self.camera.m_view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.m_proj * m_view))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)


















