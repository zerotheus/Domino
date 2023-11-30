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
    buxaDeSena:Peca = None 
    pecaLivreLadoEsquerdo:Peca = None#pra cima esquerda
    pecaLivreLadoDireito:Peca = None#pra cima direita
    pecasParaSortear:list[Peca] = []
    participantes = []
    jogador = None

    IMAGEM_DE_FUNDO = pygame.image.load(os.path.join('Domino\pecasDomino','tela.png'))

    pygame.font.init()
    FONTE_JOGO = pygame.font.SysFont('arial',50)

    def __init__(self) -> None:
        self.caixaDeDomino = CaixaDeDomino()
        print(self.caixaDeDomino)
        self.jogador = Jogador("Sofia dahPuta")
        self.addParticipante(self.jogador)
        self.addParticipante(Jogador("Yasmin Yaz Bollaz"))
        self.addParticipante(Jogador("Shotaberta"))
        self.addParticipante(Jogador("PowerGuido"))     
        self.pecasParaSortear = self.caixaDeDomino.getPecas()
        self.buxaDeSena = self.pecasParaSortear[27]
        pass
    
    def iniciar(self):
        self.quantidadeDePecas()
        self.embaralhar()
        self.quantidadeDePecas()
        inicianteIndex=self.defineOrdemDeJogada()
        self.participantes[inicianteIndex].executaPrimeiraJogada()
        self.participantes[inicianteIndex].listarMinhasPecas()
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
    
    def embaralhar(self):
        for participante in self.participantes:
            self.entregePecas(participante)
        pass
    
    def entregePecas(self,participante):
        pecas = self.pecasParaSortear #TODO alterar como funciona
        for i in range (0,7):
            index = random.randint(0,len(pecas) - 1)
            peca = pecas[index]
            participante.setPeca(peca)
            pecas.remove(peca)
        pass
    
    def getJogador(self):
        return self.jogador
    
    def quantidadeDePecas(self):
        print("pecas em jogo",len(self.pecasParaSortear))
    
    def defineOrdemDeJogada(self):
        index = self.pegajogadorComMaiorBuxa()
        print("Jogador", index , "tem a buxa de sena")
        return index

    
    def pegajogadorComMaiorBuxa(self):
        for i in range (0,4):
            if(self.participantes[i].tenhoBuxa() == self.buxaDeSena):
                return i
    
    def aindaEhPossivelDeJogar(self):
        pass