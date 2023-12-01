import time
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
        self.pecasNaEsq:list[Peca] = [] 
        self.pecasNaDir:list[Peca] = [] 
        self.participantes:list[Jogador] = []
        self.caixaDeDomino:CaixaDeDomino = CaixaDeDomino()
        self.jogador = Jogador("Sofia dahPuta")
        self.addParticipante(self.jogador)
        self.addParticipante(Jogador("Yasmin Yaz Bollaz"))
        self.addParticipante(Jogador("Shotaberta"))
        self.addParticipante(Jogador("PowerGuido"))     
        self.pecasParaSortear = self.caixaDeDomino.getPecas()
        self.buxaDeSena:Peca = self.pecasParaSortear[27]
        self.jogadorAtual:int = 0
        self.encaixeEsquerdo = self.buxaDeSena.ladoInferior
        self.encaixeDireito = self.buxaDeSena.ladoSuperior
        self.botaoPassar = None
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
        self.jogadorAtual += 1
        if(self.participantes[self.jogadorAtual % 4] != self.jogador):
            self.iaJogue()
        pass

    def desenharTela(self):
        cenarioRetangulo = pygame.Rect(0, 0, TELA_LARGURA, TELA_ALTURA)
        tela.blit(self.IMAGEM_DE_FUNDO,cenarioRetangulo)
        self.botaoPassarVez()
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
            if(p.possoJogar(self.encaixeEsquerdo,self.encaixeDireito)):
                return True    
        return False
    
    def desEmpate(self):
        participanteComMenosPontos = self.jogador
        for p in self.participantes:
            if(p.pontosAtuais()<participanteComMenosPontos.pontosAtuais()):
                participanteComMenosPontos = p
        return participanteComMenosPontos.nome
    
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
        if self.botaoPassar.collidepoint(colisao):
            print("entrei no if")
            if not self.jogador.possoJogar(self.encaixeDireito,self.encaixeEsquerdo):
                self.jogadorAtual +=1
                self.iaJogue()
            else:
                print("voce pode jgr")
        i = 0
        for peca in self.jogador.lista_de_Pecas:
            if peca.detectaColisao(colisao):
                if self.jogador.possoJogarEssaPeca(peca,self.encaixeDireito,self.encaixeEsquerdo):
                    if(self.conectaDosDoisLados(peca)):
                        print("Foram dois")
                        self.jogador.jogadorJogue(i)
                        #TODO por a escolha nesse caso
                    elif self.encaixeDireito.conecta(peca.ladoSuperior) or self.encaixeDireito.conecta(peca.ladoInferior):
                        pecaJogada:Peca=self.jogador.jogadorJogue(i)
                        print(pecaJogada.meDeSeuLadoLivre().getValor())
                        self.encaixeDireito=pecaJogada.meDeSeuLadoLivre()
                        self.pecasNaDir.append(pecaJogada) 
                    elif self.encaixeEsquerdo.conecta(peca.ladoSuperior) or self.encaixeEsquerdo.conecta(peca.ladoInferior): 
                        pecaJogada:Peca=self.jogador.jogadorJogue(i)
                        print(pecaJogada.meDeSeuLadoLivre().getValor())
                        self.encaixeEsquerdo = pecaJogada.meDeSeuLadoLivre()
                        self.pecasNaEsq.append(pecaJogada) 
                    #self.pecasJogadas.append(peca)
                    self.jogadorAtual+=1
                    self.iaJogue()
                    return    
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
            peca.desenhar(tela,x,y,False)
    
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
                if i != 3:    
                    peca.desenharPecasAdversarios(tela,x,y,i%2!=0)
                else:
                    peca.desenharPecasAdversarios(tela,1200,y,i%2!=0)
            if(i%2!=0):
                x=475
            else:
                x+=475
                y=210
                
    def desenharPecaJogada(self,tela):
        posEsquerda = 567
        posDireita = 653
        x= 610
        y= 300   
        for peca in self.pecasJogadas:
            peca.desenhar(tela,x,y,False)
        for peca in self.pecasNaEsq:
            if not peca.ehUmaBuxa():
                peca.desenhar(tela,posEsquerda,300,True and not peca.ehUmaBuxa()) 
                posEsquerda -= 57
            else:
                posEsquerda += 15
                peca.desenhar(tela,posEsquerda,300,True and not peca.ehUmaBuxa()) 
                posEsquerda -= 42
        for peca in self.pecasNaDir:
            if not peca.ehUmaBuxa():
                peca.desenhar(tela,posDireita,300,True and not peca.ehUmaBuxa()) 
                posDireita += 57
            else:
                posDireita -= 15
                
                peca.desenhar(tela,posDireita,300,True and not peca.ehUmaBuxa())
                posDireita += 42
                
    def botaoPassarVez(self):
        self.imagem =  pygame.image.load(os.path.join('Domino\pecasDomino','passarVez.png')).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem,(60,30))  
        pos_centro_imagem = self.imagem.get_rect(topleft=(900,650)).center   
        self.botaoPassar = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem,self.botaoPassar.topleft)   