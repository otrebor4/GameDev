'''
Created on Jan 27, 2014

@author: otrebor
'''
import gameObject
import phys.physEng as physEng
import sprite


class World:
    
    def __init__(self):
        self.phyEng = physEng.PhysEng()
        
    def createWall(self, x, y, w, h, color = (0,0,0)):
        wall = gameObject.RectObject( x,y,w,h, color)
        self.phyEng.add(wall.collider)
        wall.collider.static = True
        return wall
    
    def createCircle(self, x, y, r, color = (0,0,0)):
        cir  = gameObject.CircleObject(x,y,r,color )
        self.phyEng.add(cir.collider)
        return cir
    
    def createRect(self, x,y,w,h, color = (0,0,0)):
        r = gameObject.RectObject(x,y,w,h, color)
        self.phyEng.add(r.collider)
        return r
    
    
    #not working
    
    def addSprite(self, img, x,y, w, h):
        
        sprite = sprite.Sprite( img, x, y, w, h)    
        #self.phyEng.add( sprite )
        
    