from asyncio import futures
from pickletools import pybytes
import pygame
import random
import cmCamera

vec = pygame.Vector2
FPS = 60
WIDTH = 750
HEIGHT = 600

backgroundSize = vec(10000,10000)
trajectoriesSurface = pygame.Surface(backgroundSize)

janela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Universe simulator")




clock = pygame.time.Clock()

class obj():
    def __init__(self,rx,ry,vx,vy,m) :
        self.r = vec(rx,ry)
        self.v = vec(vx,vy)
        self.m = m
        self.traj = []
    
    
    def showSelf(self):
        
        if(self.m < 100):
            pygame.draw.circle(janela,(92, 64, 51),self.r , 10)
        else:
            pygame.draw.circle(janela,(92, 64, 51),self.r , 30)
        self.r += self.v /FPS
        


    def grav(self, bodies):
        for body in bodies:
            if self != body:
                rRel = vec(body.r.x - self.r.x, body.r.y - self.r.y)
                self.v += body.m * (1/rRel.length_squared()) *rRel.normalize() *100

    def showTraj(self,trajSurf):
        
        for i in self.traj:
           # print(i)
            pygame.draw.circle(trajSurf,(0,0,100),i,2)

        

def main():
    run = True
    clock = pygame.time.Clock()
    c1 = obj(100,100,-40,-40, 1000)
    
    corpos = [c1]

    cam = cmCamera.camMov(janela, corpos, vec(WIDTH/2,HEIGHT/2))
    
    def generateSys():
        for i in range(5):
            randPos = vec(random.randint(c1.r.x - WIDTH,c1.r.x + WIDTH ) , random.randint(c1.r.y - HEIGHT,-c1.r.y + HEIGHT ) )
            randVel = vec(random.randint(c1.v.x - 100, 100-c1.v.x), random.randint(c1.v.y - 100, 100-c1.v.y))
            corpos.append(obj(randPos.x,randPos.y,randVel.x, randVel.y, 50))
            
        pass
    generateSys()
   
    while(run):
        janela.fill((0,0,0))
        janela.blit(trajectoriesSurface,(0,0))
        clock.tick(FPS)
        
        #desenha o fundo de estrelas na superficie da classe 
        cam.moveStars()
        #calculos
        cam.defineCM()
        
     
        for j in corpos:
            j.showSelf()
            j.grav(corpos)
            j.showTraj(trajectoriesSurface)
        
        
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
main()