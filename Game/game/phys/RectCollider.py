'''
Created on Jan 22, 2014

@author: otrebor
'''
import math

import game.util.Vector2 as vector2
import Collider

class RectCollider(Collider.Collider):
    
    def __init__(self, gameObject = None, x = 0, y = 0, w = 0, h = 0):
        Collider.Collider.__init__(self, gameObject)
        self.position = vector2.Vector2(x, y)
        self.h = h  # h height of the rectangle
        self.w = w  # w width of the rectangle
        self.r = math.sqrt(self.w * self.w + self.h * self.h) / 2
    
    def top(self):
        return self.position.y - self.h/2# y position
    
    def bottom(self):
        return self.top() + self.h  # y position plus height(h)
    
    def left(self):
        return self.position.x - self.w/2  # x position
    
    def right(self):
        return self.left() + self.w  # x position plus width (w)
    

    def radius(self):
        return self.r
    
        
        
        
