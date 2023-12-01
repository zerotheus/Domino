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

    IMAGEM_DE_FUNDO = pygame.image.load(os.path.join('Domino\pecasDomino','tela.png'))

    pygame.font.init()
    FONTE_JOGO = pygame.font.SysFont('arial',50)

    def __init__(self) -> None:
        self.pecasJogadas:list[Peca] = []
        self.buxaDeSena:Peca = None 
        self.pecaLivreLadoEsquerdo:Peca = None#pra cima esquerda
        self.pecaLivreLadoDireito:Peca = None#pra cima direita
        self.participantes:list[Jogador] = []
        self.caixaDeDomino = CaixaDeDomino()
        print(self.caixaDeDomino)
        self.jogador = Jogador("Sofia dahPuta")
        self.addParticipante(self.jogador)
        self.addParticipante(Jogador("Yasmin Yaz Bollaz"))
        self.addParticipante(Jogador("Shotaberta"))
        self.addParticipante(Jogador("PowerGuido"))     
        self.pecasParaSortear = self.caixaDeDomino.getPecas()
        self.buxaDeSena = self.pecasParaSortear[27]
        self.jogadorAtual:int = 0
        pass
    
    def iniciar(self):
        self.quantidadeDePecas()
        self.embaralhar()
        self.quantidadeDePecas()
        inicianteIndex=self.defineOrdemDeJogada()
        self.jogadorAtual = inicianteIndex
        self.participantes[inicianteIndex].listarMinhasPecas()
        self.pecaLivreLadoDireito = self.participantes[inicianteIndex].executaPrimeiraJogada()
        self.pecaLivreLadoEsquerdo = self.pecaLivreLadoDireito
        self.pecasJogadas.append(self.buxaDeSena)
        self.participantes[inicianteIndex].listarMinhasPecas()
        pass

    def desenharTela(self):
        cenarioRetangulo = pygame.Rect(0, 0, TELA_LARGURA, TELA_ALTURA)
        tela.blit(self.IMAGEM_DE_FUNDO,cenarioRetangulo)
        self.desenharPecasdoJogador(tela)
        self.desenharPecasdoAdversario(tela)
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
        for p in self.participantes:
            if(p.possoJogar(self.pecaLivreLadoEsquerdo.meDeSeuLadoLivre(),self.pecaLivreLadoDireito.meDeSeuLadoLivre())):
                return True
        return False
    
    def alguemVenceu(self):
        for particpante in self.participantes:
            if(len(particpante.lista_de_Pecas) == 0):
                return True
        return False
    
    def autoPlay(self):
        i = 0
        passaramAvez = 0
        while((not self.alguemVenceu()) and self.participantes[self.jogadorAtual %4] != self.jogador):
            p = self.participantes[self.jogadorAtual %4]
            passou=p.iaJogue(self.pecaLivreLadoEsquerdo,self.pecaLivreLadoDireito,self)
            print("out",self.pecaLivreLadoDireito)
            print("out",self.pecaLivreLadoEsquerdo)
            self.jogadorAtual+=1
            i+=1
            print(i)
            if(passou):
                passaramAvez+=1
                if(passaramAvez == 4):
                    print("todos passaram")
                    return
            else:
                passaramAvez = 0
        print(self.alguemVenceu())
        print()
        print(i)