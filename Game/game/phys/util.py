'''
Created on Jan 22, 2014

@author: otrebor
'''
import math

import circle
import rect


def circleToRect(c):
    pos = c.pos
    r = c.radius
    return rect.RectCollider(None, pos.x - r, pos.y - r, r + r, r + r )

def rectToCircle(r):
    return circle.CircleCollider(None, r.pos(), r.radius )

def getCollisionPosition(r1, r2):
    hitRight = r2.left() - r1.right()  #distance between edges
    hitLeft =  r1.left() - r2.right()  #distance between edge 
    
    
    if hitRight <= 0 and hitLeft <= 0: #other box is bigger and box edges is inside the box
        hitRight,hitLeft = 0,0
    
    hitTop = r1.top() - r2.bottom()
    hitBot = r2.top() - r1.bottom() 
    
    if hitTop <= 0 and hitBot <= 0:   #other box is bigger and box edges are inside
        hitTop,hitBot = 0,0
    x = (-hitRight) if hitRight < 0 else (hitLeft if hitLeft < 0 else 0)
    y = (-hitBot )  if hitBot   < 0 else (hitTop if hitTop   < 0 else 0)
    
    x,y = x,0 if math.fabs(x) > math.fabs(y) else 0,y
    return (x,y)
    
def getCollisionPosition2(r1, r2):
    hitRight = r2.left() - r1.right()  #distance between edges
    hitLeft =  r1.left() - r2.right()  #distance between edge 
    
    
    if hitRight <= 0 and hitLeft <= 0: #other box is bigger and box edges is inside the box
        hitRight,hitLeft = 0,0
    
    hitTop = r1.top() - r2.bottom()
    hitBot = r2.top() - r1.bottom() 
    
    if hitTop <= 0 and hitBot <= 0:   #other box is bigger and box edges are inside
        hitTop,hitBot = 0,0
    x = (-hitRight) if hitRight < 0 else (hitLeft if hitLeft < 0 else 0)
    y = (-hitBot )  if hitBot   < 0 else (hitTop if hitTop   < 0 else 0)
    
    return (x,y)



def collideCircleCirlce(c1,c2):
    
    pass

def collideRectRect(r1, r2):
    hit = getCollisionPosition()
    pass

def collideRectCircle(c1,r2):
    
    pass