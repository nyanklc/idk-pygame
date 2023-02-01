import random
import math
from window import Window

"""TODO: add input safety, implement sim"""
"""mode: sim/init"""
def getInput(mode : str):
    if mode == "init":
        robots = input("input number of robots")
        return 1 if robots <= 0 else robots
    elif mode == "sim":
        pass

def distance(first:tuple, second:tuple):
    return math.hypot(first[0] - second[0], first[1] - second[1])

def checkRandomRadius(positions, x, y, radius):
    for pos in positions:
        if distance((x,y), pos) < radius:
            return False
    return True

"""returns random x,y tuples in a rectangular area that do not lie within 
   a radius with each other"""
"""not checking if possible at all"""
def getRandomPositions(
    count:int, 
    minx:int, 
    maxx:int, 
    miny:int,
    maxy:int, 
    radius:float
    ):
    positions = [(random.randint(minx, maxx), random.randint(miny, maxy))]
    c = 1
    while c != count:
        x, y = random.randint(min, max), random.randint(min, max)
        if not checkRandomRadius(positions, x, y, radius):
            continue
        positions.append((x, y))
        c += 1
    return positions

def getOrientedRectangle(x, y, angle, width, height):    
    from math import cos, sin
    Top_Right_x = x + ((width / 2) * cos(angle)) - ((height / 2) * sin(angle))
    Top_Right_y = y + ((width / 2) * sin(angle)) + ((height / 2) * cos(angle))
    Top_Left_x = x - ((width / 2) * cos(angle)) - ((height / 2) * sin(angle))
    Top_Left_y = y - ((width / 2) * sin(angle)) + ((height / 2) * cos(angle))
    Bot_Left_x = x - ((width / 2) * cos(angle)) + ((height / 2) * sin(angle))
    Bot_Left_y = y - ((width / 2) * sin(angle)) - ((height / 2) * cos(angle))
    Bot_Right_x = x + ((width / 2) * cos(angle)) + ((height / 2) * sin(angle))
    Bot_Right_y = y + ((width / 2) * sin(angle)) - ((height / 2) * cos(angle))
    return ((Top_Right_x, Top_Right_y), (Top_Left_x, Top_Left_y), (Bot_Left_x, Bot_Left_y), (Bot_Right_x, Bot_Right_y))
