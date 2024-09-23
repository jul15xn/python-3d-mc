from numba import njit
import numpy as np
import glm
import math

# Screen resolution
WIN_RES = glm.vec2(1600, 900)

# Color
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)