import pygame
import os
import random
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

    while rodando:
        relogio.tick(30)
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
    
start()