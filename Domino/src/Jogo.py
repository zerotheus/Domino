import pygame
import os
import random, time
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
        self.participantes:list[Jogador] = []
        self.caixaDeDomino:CaixaDeDomino = CaixaDeDomino()
        print(self.caixaDeDomino)
        self.jogador = Jogador("Sofia dahPuta")
        self.addParticipante(self.jogador)
        self.addParticipante(Jogador("Yasmin Yaz Bollaz"))
        self.addParticipante(Jogador("Shotaberta"))
        self.addParticipante(Jogador("PowerGuido"))     
        self.pecasParaSortear = self.caixaDeDomino.getPecas()
        self.buxaDeSena:Lado = self.pecasParaSortear[27]
        self.encaixeDireito:Lado=self.buxaDeSena.ladoSuperior
        self.encaixeEsquerdo:Lado = self.buxaDeSena.ladoInferior
        self.jogadorAtual:int = 0
        pass
    
    def iniciar(self):
        self.quantidadeDePecas()
        self.embaralhar()
        self.quantidadeDePecas()
        inicianteIndex=self.defineOrdemDeJogada()
        self.desenharTela()
        self.jogadorAtual = inicianteIndex
        self.pecaJogada = self.participantes[inicianteIndex].executaPrimeiraJogada()
        self.pecasJogadas.append(self.buxaDeSena)
        self.jogadorAtual += 1
        if(self.participantes[self.jogadorAtual % 4] != self.jogador):
            self.iaJogue()
        pass

    def desenharTela(self):
        cenarioRetangulo = pygame.Rect(0, 0, TELA_LARGURA, TELA_ALTURA)
        tela.blit(self.IMAGEM_DE_FUNDO,cenarioRetangulo)
        self.desenharPecasdoJogador(tela)
        self.desenharPecasdoAdversario(tela)
        self.desenharPecaJogada(tela)
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
            if(p.possoJogar(self.encaixeEsquerdo.meDeSeuLadoLivre(),self.encaixeDireito.meDeSeuLadoLivre())):
                return True
        return False
    
    def alguemVenceu(self):
        for particpante in self.participantes:
            if(len(particpante.lista_de_Pecas) == 0):
                return True
        return False
    
    def iaJogue(self):
        i = 0
        passaramAvez = 0
        self.desenharTela()
        while((not self.alguemVenceu()) and self.participantes[self.jogadorAtual %4] != self.jogador):
            p = self.participantes[self.jogadorAtual %4]
            time.sleep(1)
            print(self.jogadorAtual % 4)
            passou=p.iaJogue(self.encaixeEsquerdo,self.encaixeDireito,self)
            self.desenharTela()
            self.jogadorAtual+=1
            i+=1
            print(i)
            if(passou):
                passaramAvez+=1
                if(passaramAvez == 3):
                    return
            else:
                passaramAvez = 0
        print(self.alguemVenceu())
        print(i)
        
    def adicionaNasJogadas(self,peca):
        self.pecasJogadas.append(peca)
        
    def detectaColisao(self,colisao):
        i = 0
        print(self.encaixeDireito == self.encaixeEsquerdo)
        for peca in self.jogador.lista_de_Pecas:
            if peca.detectaColisao(colisao):
                if self.jogador.possoJogarEssaPeca(peca,self.encaixeDireito,self.encaixeEsquerdo):
                    if(self.conectaDosDoisLados(peca)):
                        print("Foram dois")
                        self.jogador.jogadorJogue(i,self.encaixeDireito)
                    elif self.encaixeDireito.conecta(peca.ladoSuperior) or self.encaixeDireito.conecta(peca.ladoInferior):
                        pecaJogada:Peca=self.jogador.jogadorJogue(i,self.encaixeDireito)
                        print(pecaJogada.meDeSeuLadoLivre().getValor())
                        self.encaixeDireito=pecaJogada.meDeSeuLadoLivre()
                    elif self.encaixeEsquerdo.conecta(peca.ladoSuperior) or self.encaixeEsquerdo.conecta(peca.ladoInferior): 
                        pecaJogada:Peca=self.jogador.jogadorJogue(i,self.encaixeEsquerdo)
                        print(pecaJogada.meDeSeuLadoLivre().getValor())
                        self.encaixeEsquerdo = pecaJogada.meDeSeuLadoLivre()
                    self.pecasJogadas.append(peca)    
            i+=1
    
    def conectaDosDoisLados(self,peca:Peca):
        if(peca.ladoSuperior.getValor() == self.encaixeDireito.getValor()
           and peca.ladoInferior.getValor() == self.encaixeEsquerdo.getValor()):
            return True    
        return False    
        
    def desenharPecasdoJogador(self,tela):
        x = 475
        y = 635
        for peca in self.jogador.lista_de_Pecas:
            x += 35 
            peca.desenhar(tela,x,y)
    
    def desenharPecasdoAdversario(self,tela):
        x = 40
        y = 210
        for i in range(1,4):
            for peca in self.participantes[i].lista_de_Pecas:
                if(i%2!=0):
                    y+=35
                else:
                    x+=35
                    y = 30       
                peca.desenharPecasAdversarios(tela,x,y,i%2!=0)
            if(i%2!=0):
                x=475
            else:
                x+=475
                y=210
                
    def desenharPecaJogada(self,tela):
        x= 610
        y= 300   
        for peca in self.pecasJogadas:
            peca.desenhar(tela,x,y)
         
        