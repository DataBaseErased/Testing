import cmCamera
import pygame


vec = pygame.Vector2
clock = pygame.time.Clock()
drag = False

FPS = 60
dragFactor = 30
WIDTH = 980
HEIGHT = 720


janela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Universe simulator")


class obj():
    def __init__(self,rx,ry,vx,vy,m,radius) :
        self.r = vec(rx,ry)
        self.v = vec(vx,vy)
        self.m = m
        self.R = radius
        
    
    def showSelf(self):
        
        if(self.m < 101):
            pygame.draw.circle(janela,(92, 64, 51),self.r , self.R)
        else:
            pygame.draw.circle(janela,(255,250,134),self.r , self.R)
        self.r += self.v /FPS
        
        


    def grav(self, bodies):
        for body in bodies:
            if self != body:
                rRel = vec(body.r.x - self.r.x, body.r.y - self.r.y)
                self.v += body.m * (1/(rRel.length_squared()))*rRel.normalize() 
            


        

def main():
    run = True

    c1 = obj(100,100,10,0, 300000,25)
    c2 = obj(300, 400, 100, -120, 100,10)
    corpos = [c1, c2]

    cam = cmCamera.camMov(janela, corpos, vec(WIDTH/2,HEIGHT/2))

    while(run):
        mousePos = vec (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        janela.fill((0,0,0))
        clock.tick(FPS)
        
        #desenha o fundo de estrelas e mostra o CM. Talvez esteja debaixo da estrela
        cam.moveStars()
        cam.showCM()
            
        for corpo in corpos:
            corpo.showSelf()
            corpo.grav(corpos)
        
        #add quit game and drag screen
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    cam.is3Pressed = True
                    clickPos = vec( event.pos[0], event.pos[1])

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    cam.is3Pressed = False

            elif event.type == pygame.MOUSEMOTION and cam.is3Pressed:
                offset = mousePos - clickPos
                cam.rCM += offset/dragFactor
                for corpo in corpos:
                    corpo.r += offset/dragFactor

        pygame.display.update()
        
main()