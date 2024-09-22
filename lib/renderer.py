from dataclasses import dataclass
import math
import pygame

@dataclass
class Point3D:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

@dataclass
class Point2D:
    x: float = 0.0
    y: float = 0.0

@dataclass
class Vertex:
    start: int
    end: int

ROTATIONX = 0.0
ROTATIONY = 0.0
FOV = 10.0

def point2DtoTuple(point):
    return (point.x, point.y)

def rotateX(point):
    global ROTATIONX
    returnPoint = Point3D()
    returnPoint.x = point.x
    returnPoint.y = math.cos(ROTATIONX) * point.y - math.sin(ROTATIONX) * point.z
    returnPoint.z = math.sin(ROTATIONX) * point.y + math.cos(ROTATIONX) * point.z
    return returnPoint

def rotateY(point):
    global ROTATIONY
    returnPoint = Point3D()
    returnPoint.x = math.cos(ROTATIONY) * point.x - math.sin(ROTATIONY) * point.z
    returnPoint.y = point.y
    returnPoint.z = math.sin(ROTATIONY) * point.x + math.cos(ROTATIONY) * point.z
    return returnPoint

def projection(point):
    global RENDER_SIZE
    return Point2D(RENDER_SIZE[0] / 2 + (FOV * point.x) / (FOV + point.z) * 100, RENDER_SIZE[1] / 2 + (FOV * point.y) / (FOV + point.z) * 100)

def RenderInit(window):
    global RENDER_WIN, RENDER_SIZE
    RENDER_WIN = window
    RENDER_SIZE = RENDER_WIN.get_size()

def Render(deltaTime: float, points: list[Point2D], vertices: list[Vertex]):
    global ROTATIONY, RENDER_SIZE
    RENDER_SIZE = RENDER_WIN.get_size()

    for vertex in vertices:
        rotatedStartPoint = rotateX(rotateY(points[vertex.start]))
        rotatedEndPoint = rotateX(rotateY(points[vertex.end]))
        start = projection(rotatedStartPoint)
        end = projection(rotatedEndPoint)
        pygame.draw.line(RENDER_WIN, (255, 255, 255), point2DtoTuple(start), point2DtoTuple(end))