import perlin_noise as pn

class Noise:
    def __init__(self, seed=0):
        self.ctx = {}
        self.ctx[0] = pn.PerlinNoise(octaves=3, seed=seed)
        self.ctx[1] = pn.PerlinNoise(octaves=6, seed=seed)
        self.ctx[2] = pn.PerlinNoise(octaves=12, seed=seed)
        self.ctx[3] = pn.PerlinNoise(octaves=24, seed=seed)

    def noise_val(self, x, z):
        x /= 100
        z /= 100

        noise_val = self.ctx[0]([x, z])
        noise_val += 0.5 * self.ctx[1]([x, z])
        noise_val += 0.25 * self.ctx[2]([x, z])
        noise_val += 0.125 * self.ctx[3]([x, z])

        noise_val *= 10
        noise_val = round(noise_val)

        return noise_val
