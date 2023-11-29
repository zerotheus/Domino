import pygame
import os
import random
from Settings.Configuration import pygame, clock, SCREEN_UPDATE

TELA_LARGURA = 1280
TELA_ALTURA = 720
IMAGEM_DE_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join('pecasDomino','tela.png')))

pygame.font.init()
FONTE_JOGO = pygame.font.SysFont('arial',50)

def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame.gameOver()
            if event.type == SCREEN_UPDATE:
                mainGame.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainGame.keyInput(event)
            mainGame.draw()
            pygame.display.update()
            clock.tick(60)

loop = asyncio.get_event_loop()