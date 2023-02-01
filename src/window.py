import pygame
from globals import WINDOW_AGENT_COLOR, WINDOW_MASTER_COLOR

class Window:
    def __init__(self, minx, maxx, miny, maxy):
        self.color_master = WINDOW_MASTER_COLOR
        self.color_agent = WINDOW_AGENT_COLOR
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

        pygame.init()

        # stupid pygame crashes x11?
        background_color = (234, 212, 252)
        # create window
        self.screen = pygame.display.set_mode([maxx - minx, maxy - miny])
        pygame.display.set_caption('master-agent-sim')
        self.screen.fill(background_color)
        pygame.display.flip()

    def draw(self, master, agents):
        self.draw(master, self.color_master)
        for agent in agents:
            self.draw(agent, self.color_agent)
        # TODO: add vision areas (sight)
        pygame.display.flip()

    def draw(self, robot, color):
        pygame.draw.polygon(self.screen, color, robot.rect)
        pygame.display.flip()

    # TODO:
    def drawSight(robot, color):
        pass


