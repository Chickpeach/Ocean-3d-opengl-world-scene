from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
                
        # columns
        #for i in range(9):
            #add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            #add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        add(Cat(app, pos=(0, 0.5, -10)))

        #coral
        add(Coral(app, pos=(64, -2, 0)))
        add(Coral(app, pos=(90, -2, 0)))
        add(Coral(app, pos=(85, 33, 13)))  # มุมซ้ายบน ขนาดใหญ่
        add(Coral(app, pos=(60, 33, -20)))
        add(Coral(app, pos=(92, 33, -20)))
        add(Coral(app, pos=(92, 33, 14)))
        add(Coral(app, pos=(82, 33, -14)))
        add(Coral(app, pos=(58, 33, 19)))
        add(Coral(app, pos=(55, 33, 15)))
        
        #kelp
        add(Kelp(app, pos=(5, -32.9, -1)))
        add(Kelp(app, pos=(-13, -32.9, -1)))
        add(Kelp(app, pos=(-18, -32.9, -7)))
        add(Kelp(app, pos=(10, -32.9, -20)))
        add(Kelp(app, pos=(-19, -32.9, -19.8), rot=(0, 15, 0)))
        add(Kelp(app, pos=(14, -32.9, 10)))
        add(Greenkelp(app, pos=(11, 0.5, -14)))
        add(Greenkelp(app, pos=(-11, 0.5, -14)))
        add(Greenkelp(app, pos=(-11, 0.5, 1)))
        add(Greenkelp(app, pos=(-13, 0.5, 16), rot=(0, 90, 0)))
        add(Greenkelp(app, pos=(13, 0.5, 16), rot=(0, 180, 0)))
        add(Greenkelp1(app, pos=(11, 0, 1)))
        add(Greenkelp1(app, pos=(15, 0, 10)))
        add(Greenkelp1(app, pos=(13, 0, 10)))
                
        #clam
        add(Clam(app, pos=(0, 2, 13)))
        add(Clam(app, pos=(-12, 2, -10), rot=(0, 90, 0)))
        
        #pushilin
        add(Pushilin(app, pos=(-16, 1.1, 13)))
        add(Pushilin(app, pos=(7, 0.5, 13), scale=(2.5, 2.5, 2.5)))
        add(Pushilin(app, pos=(16, 1.1, -13)))
        add(Pushilin(app, pos=(5, 0, -13), scale=(2, 2, 2)))
        add(Ice(app, pos=(-8, -0.5, -13), rot=(0, 90, 0)))
        add(Ice(app, pos=(-10, -0.5, -2), rot=(0, 90, 0)))
        add(Ice(app, pos=(-8, -0.5, -1.5), rot=(0, 180, 0)))
        
        #octopus
        add(Octopus(app, pos=(13, 1.2, -5)))
        add(Squid(app, pos=(-18, -1, 5), rot=(0, 45, 0)))
    
        #goldfish
        add(Goldfish(app, pos=(4, 1.2, -20), rot=(0, 250, 0)))
        add(Goldfish(app, pos=(-15, 5, -5)))
        add(Goldfish(app, pos=(-20, 0.5, -5), rot=(0, 60, 0)))
        add(Goldfish(app, pos=(5, 0.5, 1), rot=(0, 100, 0)))
        add(Goldfish(app, pos=(12, 2, -12), rot=(0, 150, 0)))
        
        #shark
        add(Shark(app, pos=(-11, 8, 12), rot=(0, 150, 0)))
        add(Shark(app, pos=(11, 10, -12), rot=(0, 100, 0)))
        
        #salmon
        add(Salmon(app, pos=(9, 5, -5), rot=(0, 150, 0)))
        add(Salmon(app, pos=(-9, 5, -5), rot=(0, 95, 0)))
        add(Salmon(app, pos=(-1, 3, 20), rot=(0, 76, 0)))
        
        #whale
        add(Whale(app, pos=(-25, 10, 12), rot=(0, 150, 0)))
        add(Whale(app, pos=(27, 10, 15), rot=(0, 100, 0)))
        
        #hibiscus
        add(Hibiscus(app, pos=(17, 0.05, 6)))
        add(Hibiscus(app, pos=(1, 0.05, -6)))
        add(Hibiscus(app, pos=(-20, 0.05, -10)))
        add(Hibiscus(app, pos=(5, 0.05, 9)))
        add(Hibiscus(app, pos=(3.5, 0.05, -8)))
        add(Hibiscus(app, pos=(-13, 0.05, 10)))
        
        #crayfish
        add(Crayfish(app, pos=(-5, -1, 10), rot=(0, 76, 0)))
        add(Crayfish(app, pos=(-6, -1, -14), rot=(0, 180, 0)))
        add(Crayfish(app, pos=(0, -1, 1), rot=(0, 210, 0)))
        
        #sand
        add(Sand(app, pos=(8.5, 0.5, 9.5), rot=(0, 210, 0)))
        add(Sand(app, pos=(-11, 0.5, 11), rot=(0, 210, 0)))
        add(Sand(app, pos=(-11, 0.5, 3), rot=(0, 140, 0)))
        add(Sand(app, pos=(-18, 0.5, -8), rot=(0, 140, 0)))
        add(Sand(app, pos=(13, 0.5, 5), rot=(0, 210, 0)))
        add(Sand(app, pos=(15, 0.5, -17), rot=(0, 210, 0)))
        
        #turtle
        add(Turtle(app, pos=(-5, 0, 1), rot=(0, 210, 0)))
        add(Turtle(app, pos=(-8, 0, -6), rot=(0, 95, 0)))
        add(Turtle(app, pos=(0, 0, -17), rot=(0, 45, 0)))

    def update(self):
        pass
