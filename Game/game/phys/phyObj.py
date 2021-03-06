'''
Created on Jan 22, 2014

@author: otrebor
'''
from game.util.vector2 import Vector2
from game.gameObject import Component

'''
physical object template
'''
class Collider(Component):
    def __init__(self, gameObject):
        Component.__init__(self, gameObject)
        #my change to separate component
        self.position = Vector2()
        self.speed = Vector2() #initialize velocity to zero
        self.static =  False
        
    def pos(self):
        return self.position
    
    def setPos(self, pos):
        self.position = pos
    
    #must move to other script
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def update(self,delta):
        if not self.static:
            self.position = self.position.add( self.speed.scale(delta))
        pass