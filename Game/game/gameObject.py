'''
Created on Jan 27, 2014

@author: otrebor
'''
import pygame

import phys.rect
import util


class Object():
    pass
class Component():
    def __init__(self, gameObject):
        self.gameObject = gameObject
        
class GameObject():
    def __init__(self):
        self.collider = None
        self.render = None
        self.components = []
        
    def setPos(self,pos):
        if self.collider != None:
            self.collider.setPos(pos)
            
    def setVel(self, vel):
        if self.collider != None:
            self.collider.setVel(vel)
    
    def addVel(self, acc):
        if self.collider != None:
            self.collider.addVel(acc)
    
    '''
        Component is a lambda self,delta: {}
    '''
    def addComponent(self, component):
        if component != None:
            self.components.append(component)
    
    def update(self,delta):
        for c in self.components:
            if c != None and c.update != None:
                c.update(delta)
        
    def draw(self,screen):
        if self.render != None:
            self.render.draw(screen)

class RectObject( GameObject ):
    def __init__(self, x,y, w, h, collor):
        self.collor = collor
        self.collider = phys.rect.RectCollider(x,y,w,h )
        self.render = Object()
        self.render.draw = lambda screen: self.drawRect(screen)
        self.pos =  lambda: self.collider.pos()
        
        
    def rect(self):
        return pygame.rect.Rect( self.collider.x,self.collider.y, self.collider.w, self.collider.h)
        
    def drawRect(self,screen):
        pygame.draw.rect(screen,self.collor, self.rect() )
        
class CircleObject( GameObject ):
    def __init__(self, x, y, r, collor):
        self.collor = collor
        self.collider = phys.circle.CircleCollider( util.vector2.Vector2( x,y),r)
        self.render = Object()
        self.render.draw = lambda screen: self.drawCircle(screen)
        self.pos = lambda: self.collider.pos()
        
        
    def drawCircle(self, screen):
        pygame.draw.circle( screen, self.collor, (self.collider.pos().x, self.collider.pos().y), self.collider.r)
        
        
        
        
        
        