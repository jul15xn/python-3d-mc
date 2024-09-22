from lib.renderer import *

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

def RenderLevel(dt):
    global POINTS, VERTICES
    Render(dt, POINTS, VERTICES)