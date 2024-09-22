from lib import window, text, renderer
import math

DEBUG_ENABLED = True
TICKSINCELASTFRAME = 0

def Tick_Debug():
    if not DEBUG_ENABLED:
        return
    fps = round(window.WIN_CLOCK.get_fps() * 10000) / 10000
    text.draw_text((0, 0), fps, 18)
    text.draw_text((0, 15), str(window.DELTATIME), 18)
    text.draw_text((0, 30), f"({renderer.ROTATIONX}, {renderer.ROTATIONY})", 18)

def DrawPointID(pointPosition: tuple[float, float], pointIndex: int):
    text.draw_text((pointPosition[0], pointPosition[1]), str(pointIndex), 18)