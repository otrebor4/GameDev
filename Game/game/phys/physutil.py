'''
Created on Jan 22, 2014

@author: otrebor
'''
import math

import CircleCollider
import game.phys.RectCollider as rect
import game.util.Vector2 as vector2


def circleToRect(c):
    pos = c.pos()
    r = c.radius
    return rect.RectCollider(None, pos.x, pos.y, r + r, r + r)

def rectToCircle(r):
    return CircleCollider.CircleCollider(None, r.pos().x, r.pos().y, r.radius())

def getCollisionPosition(r1, r2):
    hitRight = r2.left() - r1.right()  # distance between edges
    hitLeft = r1.left() - r2.right()  # distance between edge 
    
    
    if hitRight <= 0 and hitLeft <= 0:  # other box is bigger and box edges is inside the box
        hitRight, hitLeft = 0, 0
    
    hitTop = r2.top() - r1.bottom()
    hitBot = r1.top() - r2.bottom() 
    
    if hitTop <= 0 and hitBot <= 0:  # other box is bigger and box edges are inside
        hitTop, hitBot = 0, 0
    x = (-hitRight) if hitRight < 0 else (hitLeft if hitLeft < 0 else 0)
    y = (-hitBot)  if hitBot < 0 else (hitTop if hitTop < 0 else 0)
    
    if math.fabs(x) > math.fabs(y):
        x,y = x,0
    else:
        x,y = 0,y
    
    return (x, y)
    
def getCollisionPosition2(r1, r2):
    hitRight = r2.left() - r1.right()  # distance between edges
    hitLeft = r1.left() - r2.right()  # distance between edge 
    
    
    if hitRight <= 0 and hitLeft <= 0:  # other box is bigger and box edges is inside the box
        hitRight, hitLeft = 0, 0
    
    hitTop = r1.top() - r2.bottom()
    hitBot = r2.top() - r1.bottom() 
    
    if hitTop <= 0 and hitBot <= 0:  # other box is bigger and box edges are inside
        hitTop, hitBot = 0, 0
    x = (-hitRight) if hitRight < 0 else (hitLeft if hitLeft < 0 else 0)
    y = (-hitBot)  if hitBot < 0 else (hitTop if hitTop < 0 else 0)
    
    return (x, y)

def collideCircleCirlce(c1, c2):
    x = c1.pos().sub(c2.pos())
    x = x.normalize()
    v1 = c1.speed
    x1 = x.dot(v1)
    v1x = x.scale(x1)
    v1y = v1.sub(v1x)
    
    x = x.scale(-1)
    
    v2 = c2.speed
    x2 = x.dot(v1)
    v2x = x.scale(x2)
    v2y = v2.sub(v2x)
    
    m1, m2 = c1.mass(), c2.mass()
    cm = m1 + m2
    
    nV1 = v1x.scale((m1 - m2) / cm).add(v2x.scale((2 * m2) / cm)).add(v1y)
    nV2 = v1x.scale((2 * m1) / cm).add(v2x.scale((m2 - m1) / cm)).add(v2y)
    
    c1.setSpeed(nV1)
    c2.setSpeed(nV2)
    
def collideRectRect(r1, r2):
    hit = getCollisionPosition(r1, r2)
    m1 = r1.mass()
    m2 = r2.mass()
    mt = m1 + m2
    v1x, v1y, v2x, v2y = r1.speed.x, r1.speed.y, r2.speed.x, r2.speed.y
    if hit[0] != 0:  # hit right or left
        v1x = ((m1 - m2) / mt) * v1x + (2 * m2 / mt) * v2x
        v2x = ((2 * m2 / mt) * v1x) + ((m1 - m2) / mt) * v2x
    if hit[1] != 0:  # hit top or bot
        v1y = ((m1 - m2) / mt) * v1y + (2 * m2 / mt) * v2y
        v2y = ((2 * m2 / mt) * v1y) + ((m1 - m2) / mt) * v2y
    r1.setSpeed(vector2.Vector2(v1x, v1y))
    r2.setSpeed(vector2.Vector2(v2x, v2y))

def collideCircleRect(c1, r2):
    hit = getCollisionPosition2(circleToRect(c1), r2)
    m1 = c1.mass()
    m2 = r2.mass()
    mt = m1 + m2
    v1x, v1y, v2x, v2y = c1.speed.x, c1.speed.y, r2.speed.x, r2.speed.y
    
    
    if hit[0] != 0:  # hit right or left
        v1x = ((m1 - m2) / mt) * v1x + (2 * m2 / mt) * v2x
        v2x = ((2 * m2 / mt) * v1x) + ((m1 - m2) / mt) * v2x
    if hit[1] != 0:  # hit top or bot
        v1y = ((m1 - m2) / mt) * v1y + (2 * m2 / mt) * v2y
        v2y = ((2 * m2 / mt) * v1y) + ((m1 - m2) / mt) * v2y
    c1.setSpeed(vector2.Vector2(v1x, v1y))
    r2.setSpeed(vector2.Vector2(v2x, v2y))
