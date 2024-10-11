# Example file showing a basic pygame "game loop"
import pygame


# pygame setup
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((500, 500)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Velha') #nome da janela
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 30) #importar 
running = True #variavel de controle do status do jogo

personagem_x = fonte_quadrinhos.render('Δ', True, 'red')
personagem_y = fonte_quadrinhos.render('o', True, 'red')
cor_fundo = 1

while running:
    # controle de evento do jogo
    # pygame.QUIT 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1
 
    if cor_fundo == 1:
       # screen.fill('blue')
       screen.blit(personagem_x,(240,240))
    elif cor_fundo == 2:
       # screen.fill('red')
       screen.blit(personagem_y,(240,240))
    else:
       screen.fill('purple')


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()