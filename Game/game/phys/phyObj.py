'''
Created on Jan 22, 2014

@author: otrebor
'''
from circle import CircleCollider

class phyObj:
    def __init__(self):
        pass
    
    
    
    def checkCollision(self,obj):
        if isinstance(obj,CircleCollider):
            return self.checkCircleCollision(obj)
        return False