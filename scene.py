from model import *

class Scene:
    def __init__(self, app) :
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, index):
        self.objects.remove(self.objects[index])

    def clear_scene(self):
        self.objects.clear()

    def load(self):
        app = self.app
        add = self.add_object

        percent = 0
        n = 50
        totalpercent = (2 * n) **2
        for x in range(-n, n):
            for z in range(-n, n):
                perlin_value = app.noise.noise_val(x, z)
                for y in range(5):
                    add(Cube(app, pos=(x, perlin_value-y, z),scale=(0.5,0.5,0.5)))

                percent += (1 / totalpercent) * 100
                print(f'{percent}%')

    def render(self):
        for obj in self.objects:
            obj.render()