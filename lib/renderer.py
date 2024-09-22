from dataclasses import dataclass
import math
import pygame
from lib import debug
import random

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
class Face:
    topRight: int
    bottomRight: int
    bottomLeft: int
    topLeft: int
    color: tuple = (255, 255, 255)

@dataclass
class Vertex:
    start: int
    end: int

ROTATIONX = 0.0
ROTATIONY = 0.0
FOV = 10.0

def point2DtoTuple(point: Point2D):
    return (point.x, point.y)

def rotateX(point: Point3D):
    global ROTATIONX
    returnPoint = Point3D()
    returnPoint.x = point.x
    returnPoint.y = math.cos(ROTATIONX) * point.y - math.sin(ROTATIONX) * point.z
    returnPoint.z = math.sin(ROTATIONX) * point.y + math.cos(ROTATIONX) * point.z
    return returnPoint

def rotateY(point: Point3D):
    global ROTATIONY
    returnPoint = Point3D()
    returnPoint.x = math.cos(ROTATIONY) * point.x - math.sin(ROTATIONY) * point.z
    returnPoint.y = point.y
    returnPoint.z = math.sin(ROTATIONY) * point.x + math.cos(ROTATIONY) * point.z
    return returnPoint

def projection(point: Point3D):
    global RENDER_SIZE
    return Point2D(RENDER_SIZE[0] / 2 + (FOV * point.x) / (FOV + point.z) * 100, RENDER_SIZE[1] / 2 + (FOV * point.y) / (FOV + point.z) * 100)

def RenderInit(window):
    global RENDER_WIN, RENDER_SIZE
    RENDER_WIN = window
    RENDER_SIZE = RENDER_WIN.get_size()

def UpdateSize():
    global RENDER_SIZE
    RENDER_SIZE = RENDER_WIN.get_size()

def RenderWireFrame(points: list[Point2D], vertices: list[Vertex]):
    for vertex in vertices:
        rotatedStartPoint = rotateX(rotateY(points[vertex.start]))
        rotatedEndPoint = rotateX(rotateY(points[vertex.end]))
        start = point2DtoTuple(projection(rotatedStartPoint))
        end = point2DtoTuple(projection(rotatedEndPoint))

        if debug.DEBUG_ENABLED:
            debug.DrawPointID(start, vertex.start)

        pygame.draw.line(RENDER_WIN, (255, 255, 255), start, end)

def RenderFaces(points: list[Point2D], faces: list[Face]):
    convertedPoints = []

    for point in points:
        convertedPoint = rotateX(rotateY(point))
        convertedPoint = point2DtoTuple(projection(convertedPoint))
        convertedPoints.append(convertedPoint)

    for face in faces:
        facePoints = []
        facePoints.append(convertedPoints[face.topRight])
        facePoints.append(convertedPoints[face.bottomRight])
        facePoints.append(convertedPoints[face.bottomLeft])
        facePoints.append(convertedPoints[face.topLeft])

        pygame.draw.polygon(RENDER_WIN, face.color, facePoints)