'''
Created on Jan 15, 2014

@author: Otrebor45
'''
import sys
import time
import pygame
import util.Vector2 as Vector2
import random
from pygame.locals import *

import world
import scripts.ClickToMove 

class Game:
    GAMENAME = "null"
    
    INIT = False        
    def __init__ (self):
        random.seed(10000)
        self.INIT = True
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption(self.GAMENAME)
        
        self.world = world.World(Vector2.Vector2(0,0))
        for i in range(0,10):
            c = self.world.createCircle(random.uniform(50,450), random.uniform(50,450), 10, (250,0,100))
            c.riged.velocity = Vector2.Vector2(random.uniform(-10,10), random.uniform(-10,10)).scale(30)
            
        r = self.world.createRect(250, 250, 25, 25, (10,10,50))
        r.addComponent(scripts.ClickToMove.ClickToMove(r) )
        r.addComponent(scripts.ClickToMove.TestMessage(r))
        self.world.createWall(1, 500, 500, 100, (0,0,0)) #bottom
        self.world.createWall(1, -100, 500, 100, (0,0,0))   #top
        self.world.createWall(-99, 0, 100, 500, (0,0,0))   #left
        self.world.createWall(500, 0, 100, 500, (0,0,0)) #right
        
        
    def draw(self, delta):
        self.screen.fill((255, 255, 0))
        self.world.draw(self.screen)
        #pygame.draw.circle(self.screen,(0,0,0), (250,250),100, 0)
        pygame.display.flip()
        return
    
    def update(self, delta):
        pygame.event.pump()
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        self.world.update(delta)
        
        return
    
    def run(self):
        if not self.INIT:
            self.init()
        oldtime = pygame.time.get_ticks()
        time.sleep(1)
        while True:
            newtime = pygame.time.get_ticks()
            delta = newtime - oldtime
            oldtime = newtime
            deltaf = delta/1000.0
            self.update(deltaf)
            self.draw(deltaf)
            
if __name__ == '__main__':
    g = Game()
    g.run()
    
        
