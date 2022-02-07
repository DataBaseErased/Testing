# Simple pygame program

# Import and initialize the pygame library
from random import randint
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
G = 1
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class bola():
    def __init__(self, x, y, vx, vy,m):
        self.r = pygame.Vector2(x,y)
        self.v = pygame.Vector2(vx,vy)
        self.a = pygame.Vector2(0,0)
        self.m = m

    def feelForce(self, rOther, mOther):
        #posição relativa
        rRel = pygame.Vector2(rOther.x - self.r.x, rOther.y - self.r.y)
        print(self.a)
        self.a =  mOther * (1/rRel.length_squared()) *rRel.normalize()*G

    def draw(self):
        pygame.draw.circle(screen, (0,0,0), (self.r), 10)
        self.r += self.v*1/FPS
        self.v += self.a*1/FPS
        
        


b1 = bola(100,100, 50, 60, 400000)
b2 = bola(400, 300,-30, 30,700000)

numeroBolas = 3
bList = []
# Run until the user asks to quit
running = True
while running:


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


# Fill the background with white
    screen.fill((255, 255, 255))


    b1.draw()
    b2.draw()


    b1.feelForce(b2.r, b2.m)
    b2.feelForce(b1.r, b1.m)



    # Flip the display
    pygame.display.flip()
    clock.tick(FPS)
# Done! Time to quit.
pygame.quit()