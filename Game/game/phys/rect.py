'''
Created on Jan 22, 2014

@author: otrebor
'''
import math

import phyObj
import game.util.vector2 as vector2

class RectCollider(phyObj.Collider):
    
    def __init__(self, gameObject, x, y, w, h):
        phyObj.Collider.__init__(self, gameObject)
        self.position = vector2.Vector2(x,y)
        self.h = h  # h height of the rectangle
        self.w = w  # w width of the rectangle
        self.r = math.sqrt( self.w*self.w + self.h*self.h)/2
    
    def top(self):
        return self.position.y  # y position
    
    def bottom(self):
        return self.top() + self.h  # y position plus height(h)
    
    def left(self):
        return self.position.x  # x position
    
    def right(self):
        return self.left() + self.w  # x position plus width (w)
    
    def pos(self):
        return (self.left()+self.w/2, self.top()+self.h/2)
    
    def radius(self):
        return self.r
    
        
        
        