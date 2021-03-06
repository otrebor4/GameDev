'''
Created on Jan 22, 2014

@author: otrebor
'''
'''
Constant for collision types,
'''

import circle
import game.util.vector2 as vector2
import rect
import util


class CollType:
    None    = 0
    Circle  = 1
    Rect    = 2
 
        
class PhysEng:
    def __init__(self):
        self.objects =[]
    
    
    def objCount(self):
        return self.objects.len()
    
    
    def add(self, obj):
        self.objects.append(obj)
        
    def remove(self, obj):
        self.objects.remove(obj)
    
    '''
    for each object in the list compared it to check if have collided with the other one
    if so, handle collision
    '''
    def update(self,delta):
        size = self.objCount()
        for i in range(0,size):
            for j in range(i,size):
                if i != j and not (self.objects[i].static and self.objects[j].static): #is not the same and are not both static
                    self.handleCollision(self.objects[i], self.objects[j])
                
    '''
    identify collision case
    '''
    def handleCollision(self,obj1, obj2):
        case = self.getCollisionType(obj1, obj2)
        
        if case[0] == CollType.None or case[1] == CollType.None:   #error
            return -1
        elif cmp(case, (CollType.Circle, CollType.Circle)):    #circle circle
            if self.checkCircleCircleCollision(obj1, obj2):
                pass
            else:
                return 0
        elif cmp(case, (CollType.Circle, CollType.Rect)):      #circle rectangle
            if self.checkCircleRectCollision(obj1, obj2):
                pass
            else:
                return 0
        elif cmp(case, (CollType.Rect, CollType.Circle)):      #rectangle circle
            if self.checkCircleRectCollision(obj2,obj1):
                pass
            else:
                return 0
        elif cmp(case, (CollType.Rect, CollType.Rect)):        #rectangle rectangle
            if self.checkRectRectCollision(obj1, obj2):
                pass
            else:
                return 0
        
        
        #handle collision
        return 0
    
    '''
    ================Collision handling push back=========
    '''
    
    
    
    '''
    ================Collision repositioning==============
    '''
    
    '''
    function to identify Collision types, 
    return (obj1CollTypeId, obj2CollTYpeId)
    '''
    def getCollisionType(self, obj1, obj2):
        x,y = 0,0
        
        if isinstance(obj1, circle.CircleCollider):     #first object is circle
            x = CollType.Circle     
        elif isinstance(obj1, rect.RectCollider):       #first object is rectangle
            x = CollType.Rect
        
        if isinstance(obj2, circle.CircleCollider): #second object is circle
            y = CollType.Circle           
        elif isinstance(obj2, rect.RectCollider):   #second object is rectangle
            y = CollType.Rect
            
        return (x,y)
    
    def fixPosCircleCircle(self, c1, c2):
        pos1 = c1.pos()
        pos2 = c2.pos()
        dif = pos2.sub(pos1)
        
        if c1.static:
            c2.setPos(pos2.add(dif))
        elif c2.static:
            c1.setPos(pos1.add(dif.scale(-1)))
        else:
            c1.setPos(pos1.add(dif.scale(-.5)) )
            c2.setPos(pos2.add(dif.scale( .5)) )
        
    def fixPosCircleRect(self, c1, r2):
        colPos = util.getCollisionPosition2(util.circleToRect(c1) , r2)
        if(colPos[0] == 0 or colPos[1] == 0 ):
            pos = vector2.Vector2(colPos[0],colPos[1])
            pos1 = c1.pos()
            pos2 = r2.pos()
            if c1.static:
                r2.setPos(pos2.add(pos))
            elif r2.static:
                r2.setPos(pos1.add(pos.scale(-1) ))
            else:
                c1.setPos(pos1.add(pos.scale(-.5)))
                r2.setPos(pos2.add(pos.scale( .5)))
        else:
            pos1 = c1.pos()
            pos2 = r2.pos()
            dif = pos2.sub(pos1)
        
            if c1.static:
                r2.setPos(pos2.add(dif))
            elif r2.static:
                c1.setPos(pos1.add(dif.scale(-1)))
            else:
                c1.setPos(pos1.add(dif.scale(-.5)) )
                r2.setPos(pos2.add(dif.scale( .5)) )
           
    def fixPosRectRect(self, r1, r2):
        colPos = util.getCollisionPosition(r1, r2)
        pos = vector2.Vector2(colPos[0],colPos[1])
        pos1 = r1.pos()
        pos2 = r2.pos()
        if r1.static:
            r2.setPos(pos2.add(pos))
        elif r2.static:
            r2.setPos(pos1.add(pos.scale(-1) ))
        else:
            r1.setPos(pos1.add(pos.scale(-.5)))
            r2.setPos(pos2.add(pos.scale( .5)))
    
    
    ''' ===============Check Collisions================'''
    
    '''
    circle vs circle collision detection
    '''
    def checkCircleCircleCollision(self, c1, c2):
        r = c1.radius + c2.radius
        r = r * r
        rsq = c1.pos.distanceSq(c2.pos)
        return r < rsq
    
    '''
    rectangle vs rectangle collision detection
    '''
    def checkRectRectCollision(self, r1, r2):
        return not ( r1.bottom() < r2.top() or 
                     r1.top()    > r2.bottom() or 
                     r1.left()   > r2.right() or
                     r1.right()  < r2.left())
        
    '''
    circle vs rectangle collision detection
    '''
    def checkCircleRectCollision(self, c,re):
        return self.checkCircleCircleCollision(c,util.rectToCircle(re) ) and self.checkRectRectCollision( util.circleToRect(),re)
    
    
    
    
    