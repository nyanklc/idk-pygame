import pygame
import math
import random

from agent import *
from master import *
from utils import *
from window import Window
from globals import *

class Sim:

    def init(self):
        self.window = Window(
            WINDOW_MINX, 
            WINDOW_MINX + WINDOW_WIDTH, 
            WINDOW_MINY, 
            WINDOW_MINY + WINDOW_HEIGHT
            )

        robots = getInput("init")
        rand_positions = getRandomPositions(len(robots), self.window, ROBOT_SPAWN_RADIUS)
        self.master = Master(rand_positions[0], random.random(-math.pi, math.pi))
        self.agents = []
        for i in range(len(robots)-1):
            self.agents.append(Agent(rand_positions[1+i], random.random(-math.pi, math.pi)))
        
        self.window.draw(self.master, self.agents)

    def start(self):
        print("hello from sim")
