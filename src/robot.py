from globals import *
from utils import getOrientedRectangle

class Robot:
    def __init__(self, x, y, yaw):
        self.pose = (x, y, yaw)
        self.width = ROBOT_WIDTH
        self.height = ROBOT_HEIGHT
        self.rect = getOrientedRectangle(x, y, yaw, self.width, self.height)

    def wanderAround():
        # TODO:
        pass
