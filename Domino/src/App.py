import pygame
import os
import random, time
from Jogo import Jogo
#from Settings.Configuration import pygame, clock, SCREEN_UPDATE

TELA_LARGURA = 1280
TELA_ALTURA = 720
# IMAGEM_DE_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join('..\pecasDomino','tela.png')))

# pygame.font.init()
# FONTE_JOGO = pygame.font.SysFont('arial',50)

def start():
    jogo = Jogo()
    relogio = pygame.time.Clock()
    
    rodando = True
    jogo.desenharTela()
    time.sleep(2)
    jogo.iniciar()
    

    while rodando:
        relogio.tick(30)
        jogo.desenharTela()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("clicou")
                jogo.detectaColisao(pygame.mouse.get_pos())
                print(jogo.encaixeDireito,jogo.encaixeEsquerdo)
    
start()