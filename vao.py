from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])

        # cat vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])

        # shadow cat vao
        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat'])

     # coral vao
        self.vaos['coral'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['coral'])

        # shadow coral vao
        self.vaos['shadow_coral'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['coral'])

     # kelp vao
        self.vaos['kelp'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['kelp'])

        # shadow coral1 vao
        self.vaos['shadow_kelp'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['kelp'])

     # greenkelp vao
        self.vaos['greenkelp'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['greenkelp'])

        # shadow greenkelp vao
        self.vaos['shadow_greenkelp'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['greenkelp'])
        
     # greenkelp1 vao
        self.vaos['greenkelp1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['greenkelp1'])

        # shadow greenkelp vao
        self.vaos['shadow_greenkelp1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['greenkelp1'])


     # clam vao
        self.vaos['clam'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['clam'])

        # shadow clam vao
        self.vaos['shadow_clam'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['clam'])

          
     # pushilin vao
        self.vaos['pushilin'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['pushilin'])

        # shadow pushilinvao
        self.vaos['shadow_pushilin'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['pushilin'])
    
     # octopus vao
        self.vaos['octopus'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['octopus'])

        # shadow octopusvao
        self.vaos['shadow_octopus'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['octopus'])

     # squid vao
        self.vaos['squid'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['squid'])

        # shadow squidvao
        self.vaos['shadow_squid'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['squid'])


     # goldfish vao
        self.vaos['goldfish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['goldfish'])

        # shadow goldfishvao
        self.vaos['shadow_goldfish'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['goldfish'])

     # shark vao
        self.vaos['shark'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['shark'])

        # shadow sharkvao
        self.vaos['shadow_shark'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['shark'])          
        

     # hibiscuss vao
        self.vaos['hibiscus'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['hibiscus'])

        # shadow hibiscusvao
        self.vaos['shadow_hibiscus'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['hibiscus'])

     # salmon vao
        self.vaos['salmon'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['salmon'])

        # shadow croissantvao
        self.vaos['shadow_salmon'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['salmon'])               

     # ice vao
        self.vaos['ice'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['ice'])

        # shadow icevao
        self.vaos['shadow_ice'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['ice'])     

     # crayfish vao
        self.vaos['crayfish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['crayfish'])

        # shadow crayfishvao
        self.vaos['shadow_crayfish'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['crayfish'])     
        
     # sand vao
        self.vaos['sand'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['sand'])

        # shadow sandvao
        self.vaos['shadow_sand'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['sand'])     
     
     # turtle vao
        self.vaos['turtle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['turtle'])

        # shadow turtlevao
        self.vaos['shadow_turtle'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['turtle'])     

     # whale vao
        self.vaos['whale'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['whale'])

        # shadow whalevao
        self.vaos['shadow_whale'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['whale'])     

     # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

     # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()