import pygame
WIDTH = 600
HEIGHT = WIDTH

pygame.init()
clock = pygame.time.Clock()
janela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Universe simulator")

font = pygame.font.SysFont(None,25)
font2 = pygame.font.SysFont(None,20)

class textInputBox():
    def __init__(self,optionBox):
        self.userText = ''
        self.inputRect = pygame.Rect(optionBox.x + optionBox.width + 10,optionBox.y,60,17)
        self.typing = False
    def updateText(self):
        pygame.draw.rect(janela, (155,255,200),self.inputRect)
        if self.userText == '':
            textSurf = font2.render('type here', True,(93,93,93))
        else:
            textSurf = font.render(self.userText, True,(0,0,0))
        janela.blit(textSurf, (self.inputRect.x,self.inputRect.y))

        

        

def drawText(text, font, color, surface, x, y):
    textobj = font.render(text,1,color)
    textRect = textobj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textobj,textRect)
    return textRect

def addBodyMenu(addBody):
    options = ["m","R", "dr/dt"]
    userInput = []
    optionsRect = []
    if addBody:
        mousePos = pygame.Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

    
        

    while addBody:
     
        menuPosition = (mousePos.x, mousePos.y,200,100)
        pygame.draw.rect(janela, (0,76,126),menuPosition)


        index = 0
        for i in options:
            optionsRect.append(drawText(i, font, (255,255,255), janela, 10 + mousePos.x, 5 + mousePos.y + 25*index))
            index += 1

        index = 0
        for elements in optionsRect:
            userInput.append(textInputBox(elements))
            userInput[index].updateText()
            index += 1

        #caixas do botões
        index = 0
        addBox = drawText("Add body", font2, (255,255,255), janela,15 + menuPosition[0],80 + menuPosition[1]) 
        trajectoryBox = drawText("Show future", font2, (255,255,255), janela, menuPosition[0] +1/2*menuPosition[2],80 + menuPosition[1])
        boxes = [addBox, trajectoryBox]
        for box in boxes:
            box.x -= 3
            box.y -= 3
            box.width +=5
            box.height += 5
            pygame.draw.rect(janela, (255,255,255), box, 2)        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.sys.exit()
            if event.type == pygame.KEYDOWN:
                for elements in userInput:
                    if elements.typing:
                        
                        if event.key == pygame.K_BACKSPACE:
                            elements.userText = elements.userText[:-1]
                        else:
                            elements.userText += event.unicode
                
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button ==1:
                    eventPos = event.pos

                    if addBox.collidepoint(eventPos):
                        myReturn = []
                        for elements in userInput:
                            intention = int(elements.userText)
                            myReturn.append(intention)
                        return myReturn
                        addBody = False
                           

                    for elements in userInput:
                        #verifica se clicou na caixa de texto
                        if elements.inputRect.collidepoint(eventPos):
                            elements.typing = True
                        else: 
                            elements.typing = False
                #cancela o menu
                if event.button == 3:
                    addBody = False

        pygame.display.update()
    
    
def main():
    addNewBody = False
    run = True

    while(run):
        clock.tick(60)
        janela.fill((0,0,0))

        addBodyMenu(addNewBody)
        addNewBody = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    addNewBody = True
        



        
        pygame.display.update()
        
main()
