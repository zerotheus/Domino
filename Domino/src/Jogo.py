import pygame
import os
import random
from Model.Lado import Lado
from Model.Peca import Peca
from Model.Tela import TELA_ALTURA, TELA_LARGURA, tela
from Model.Peca import Peca
from Model.Jogador import Jogador
from Model.CaixaDeDomino import CaixaDeDomino

class Jogo:

    caixaDeDomino:CaixaDeDomino = None
    pecasJogadas:list[Peca] = []
    participantes = []

    IMAGEM_DE_FUNDO = pygame.image.load(os.path.join('Domino\pecasDomino','tela.png'))

    pygame.font.init()
    FONTE_JOGO = pygame.font.SysFont('arial',50)

    def __init__(self) -> None:
        self.caixaDeDomino = CaixaDeDomino()
        pass

    def desenharTela(self):
        lado1 = Lado(0)
        lado2 = Lado(0)
        
        peca = Peca(lado1,lado2)
        cenarioRetangulo = pygame.Rect(0, 0, TELA_LARGURA, TELA_ALTURA)
        tela.blit(self.IMAGEM_DE_FUNDO,cenarioRetangulo)
        peca.desenhar(tela)
        pygame.display.update()

    def addParticipante(self, participante):
        self.participantes.append(participante)
        pass