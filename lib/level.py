from lib.renderer import *
from lib import debug

POINTS = [
    Point3D(-1.0, -1.0, -1.0), Point3D(-1.0, -1.0, 1.0),
    Point3D(1.0, -1.0, -1.0), Point3D(-1.0, 1.0, -1.0),
    Point3D(-1.0, 1.0, 1.0), Point3D(1.0, -1.0, 1.0),
    Point3D(1.0, 1.0, -1.0), Point3D(1.0, 1.0, 1.0)
]

VERTICES = [
    Vertex(0, 1), Vertex(0, 2), Vertex(0, 3),
    Vertex(2, 5), Vertex(3, 6), Vertex(3, 4),
    Vertex(4, 7), Vertex(6, 7), Vertex(7, 5),
    Vertex(5, 1), Vertex(4, 1), Vertex(2, 6),
]

FACES = [
    Face(0, 3, 6, 2, (225, 0, 0)), Face(2, 6, 7, 5, (225, 0, 0)),
    Face(3, 6, 7, 4, (175, 0, 0))
]

def RenderLevel():
    global POINTS, VERTICES, FACES
    UpdateSize()
    RenderFaces(POINTS, FACES)
    if debug.DEBUG_ENABLED:
        RenderWireFrame(POINTS, VERTICES)