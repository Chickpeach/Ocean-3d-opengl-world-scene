import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures['cat'] = self.get_texture(path='objects/cat/Material_baseColor.png')
        self.textures['coral'] = self.get_texture(path='objects/cat/48-3.jpg')
        self.textures['kelp'] = self.get_texture(path='objects/coral1/56-2.jpg')
        self.textures['greenkelp'] = self.get_texture(path='objects/coral1/greenkelp.png')
        self.textures['greenkelp1'] = self.get_texture(path='objects/coral1/greenkelp.png')
        self.textures['clam'] = self.get_texture(path='objects/clam/Tex_Clam.png')
        self.textures['pushilin'] = self.get_texture(path='objects/Rock/PUSHILIN_rock.png')
        self.textures['octopus'] = self.get_texture(path='objects/octopus/Tex_Octopus.png')
        self.textures['squid'] = self.get_texture(path='objects/octopus/Octopus_BaseColor.png')
        self.textures['goldfish'] = self.get_texture(path='objects/fish/Tex_Goldfish.png')
        self.textures['shark'] = self.get_texture(path='objects/fish/Tex_Shark.png')
        self.textures['hibiscus'] = self.get_texture(path='objects/flower/PUSHILIN_flower.png')
        self.textures['salmon'] = self.get_texture(path='objects/fish/Tex_Salmon.png')
        self.textures['ice'] = self.get_texture(path='objects/Rock/PUSHILIN_boulder.png')
        self.textures['crayfish'] = self.get_texture(path='objects/fish/Lobster_BaseColor.png')
        self.textures['sand'] = self.get_texture(path='objects/sand/PUSHILIN_cactus.png')
        self.textures['turtle'] = self.get_texture(path='objects/turtle/Tex_Turtle.png')
        self.textures['whale'] = self.get_texture(path='objects/whale/Tex_Whale.png')
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox2/', ext='png')
        self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        # textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]