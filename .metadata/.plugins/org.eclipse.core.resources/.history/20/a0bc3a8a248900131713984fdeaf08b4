'''
Created on Jan 27, 2014

@author: otrebor
'''
import game.base.RectObject as RectObject
import game.base.CircleObject as CircleObject
import phys.PhysEng as PhysEng
import sprite


class World:
    
    def __init__(self):
        self.phyEng = PhysEng.PhysEng()
        self.objects = []
        
    def createWall(self, x, y, w, h, color=(0, 0, 0)):
        wall = RectObject.RectObject(x, y, w, h, color)
        self.phyEng.add(wall.collider)
        wall.collider.static = True
        self.objects.append(wall)
        return wall
    
    def createCircle(self, x, y, r, color=(0, 0, 0)):
        cir = CircleObject.CircleObject(x, y, r, color)
        self.phyEng.add(cir.collider)
        self.objects.append(cir)
        return cir
    
    def createRect(self, x, y, w, h, color=(0, 0, 0)):
        r = RectObject.RectObject(x, y, w, h, color)
        self.phyEng.add(r.collider)
        self.objects.append(r)
        return r
    
    
    # not working
    
    def addSprite(self, img, x, y, w, h):
        
        sprite = sprite.Sprite(img, x, y, w, h)    
        # self.phyEng.add( sprite )
        
    def update(self, delta):
        # update game logic
        for obj in self.objects:
            obj.update(delta)
        # update physics
        self.phyEng.update(delta)
    
    def draw(self, screen):
        # call draw
        for obj in self.objects:
            obj.draw(screen)
