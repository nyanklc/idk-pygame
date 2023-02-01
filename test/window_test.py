import testing
import pygame
import random
import math

from window import Window
from agent import Agent
from master import Master

_window_size = (1000, 800)
_trials = 10
_agent_count = 5
_master_count = 3

if __name__ == "__main__":
    win = Window(0, _window_size[0], 0, _window_size[1])
    clock = pygame.time.Clock()

    for i in range(_trials):
        for k in range(_agent_count):
            x = random.randint(0, _window_size[0])
            y = random.randint(0, _window_size[1])
            sign = -1 if random.random() < 0.5 else 1
            yaw = random.random() * sign * math.pi
            agent = Agent(x, y, yaw)
            win.draw(agent, (0, 255, 0))
            # TODO:
            # win.drawSight(agent, (0, 123, 0))

        for k in range(_master_count):
            x = random.randint(0, _window_size[0])
            y = random.randint(0, _window_size[1])
            sign = -1 if random.random() < 0.5 else 1
            yaw = random.random() * sign * math.pi
            master = Master(x, y, yaw)
            win.draw(master, (0, 0, 255))

        clock.tick(2)
        

    input('end')
