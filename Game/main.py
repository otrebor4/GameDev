'''
Created on Jan 15, 2014

@author: Otrebor45
'''
import sys
import time
import pygame
import game.util.Vector2 as Vector2
import random
from pygame.locals import *

import game.world as world
from game.scripts import ClickToMove
import game.Game as Game



class Test(Game.Game):
    def __init__(self):
        self.GAMENAME = "Test Game"
        Game.Game.__init__(self)
        for i in range(0,10):
            c = self.world.createCircle(random.uniform(50,450), random.uniform(50,450), 10, (250,0,100))
            c.riged.velocity = Vector2.Vector2(random.uniform(-10,10), random.uniform(-10,10)).scale(30)
            
        r = self.world.createRect(250, 250, 25, 25, (10,10,50))
        r.addComponent(ClickToMove.ClickToMove(r) )
        r.addComponent(ClickToMove.TestMessage(r))
        self.world.createWall(1, 500, 500, 100, (0,0,0)) #bottom
        self.world.createWall(1, -100, 500, 100, (0,0,0))   #top
        self.world.createWall(-99, 0, 100, 500, (0,0,0))   #left
        self.world.createWall(500, 0, 100, 500, (0,0,0)) #right
        
            
if __name__ == '__main__':
    g = Test()
    g.run()
    
        