from __future__ import annotations
import pygame ,os, random
from Model.Lado import Lado

class Peca:
 
    def __init__(self, ladoSuperior:Lado, ladoInferior:Lado) -> None:
        self.ladoSuperior = ladoSuperior
        self.ladoInferior = ladoInferior
        self.posicaoX:float = 200
        self.posicaoY:float = 500
        self.imagens = None   
        ladoSuperior.setPeca(self)
        ladoInferior.setPeca(self)
        self.retangulo = None
        pass
    
    def setPosicaoX(self,x):
        self.posicaoX = x
    
    def getPosicaoY(self,y):
        self.posicaoY = y
    
    def conectar(self,peca:Lado) -> bool:
        return self.osLadosConectam(peca)
        
    def osLadosConectam(self,peca:Lado) -> bool:
        return self.ladoSuperior.conectaComEstaPeca(peca) or self.ladoInferior.conectaComEstaPeca(peca)
    
    def verificaSeConecta(self,peca:Lado):
        return self.ladoSuperior.verificaSemConexao(peca) or self.ladoInferior.verificaSemConexao(peca)
        
    def getConexaoSuperior(self):
        print("conexao superior")
        return self.ladoSuperior.getConexao()
        
    def ehUmaBuxa(self):
        return self.ladoSuperior.getValor() == self.ladoInferior.getValor() 
        
    def getConexaoInferior(self):
        print("conexao inferior")
        return self.ladoInferior.getConexao()
    
    def meusLadosTemValorIgual(self, ladoDireito:Lado,ladoEsquerdo:Lado):
        return self.ladoSuperior.tenhoOMesmoValor(ladoEsquerdo) or self.ladoInferior.tenhoOMesmoValor(ladoDireito) or self.ladoSuperior.tenhoOMesmoValor(ladoDireito) or self.ladoInferior.tenhoOMesmoValor(ladoEsquerdo)
            
    def getladoSuperior(self) -> Lado:
        return self.ladoSuperior
    
    def getladoInferior(self) -> Lado:
        return self.ladoInferior
    
    def meDeSeuLadoLivre(self):
        if(self.getConexaoInferior() == None):
            return self.ladoInferior
        if(self.getConexaoSuperior() == None):
            return self.ladoSuperior
    
    
    def desenhar(self,tela,x,y,rotacao):
       # self.desenharNoConsole()                                         
        self.imagem =  pygame.image.load(os.path.join('Domino\pecasDomino','peca_' + str(self.ladoSuperior.valor) + '.' + str(self.ladoInferior.valor) + '.png')).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem,(50,55))
        pos_centro_imagem = self.imagem.get_rect(topleft=(x,y)).center 
        if rotacao:
            self.imagem = pygame.transform.rotate(self.imagem,90)
        self.retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem,self.retangulo.topleft)    
    
    def desenharPecasAdversarios(self,tela,x,y,rotacao):
        #self.desenharNoConsole()                                         
        self.imagem =  pygame.image.load(os.path.join('Domino\pecasDomino','branca.png')).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem,(50,55))  
        pos_centro_imagem = self.imagem.get_rect(topleft=(x,y)).center
        if rotacao:
            self.imagem = pygame.transform.rotate(self.imagem,90)   
       
        self.retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem,self.retangulo.topleft)   
        
    def detectaColisao(self,colisao):
        if self.retangulo.collidepoint(colisao):
            print (self.desenharNoConsole())
            return self.retangulo.collidepoint(colisao)
        
    def desenharNoConsole(self):
        print("Oi sou a peça\n" + str(self.ladoSuperior.getValor()) + "\n/" + str(self.ladoInferior.getValor()))
        #print( "Sou um buxa?", self.ehUmaBuxa())
    
    