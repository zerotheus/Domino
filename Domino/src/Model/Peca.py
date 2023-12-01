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
        pass
    
    def setPosicaoX(self,x):
        self.posicaoX = x
    
    def getPosicaoY(self,y):
        self.posicaoY = y
    
    def conectar(self,peca:Peca) -> bool:
        return self.osLadosConectam(peca)
        
    def osLadosConectam(self,peca) -> bool:
        return self.ladoSuperior.conectaComEstaPeca(peca) or self.ladoInferior.conectaComEstaPeca(peca)
        
    def getConexaoSuperior(self):
        print("conexao superior")
        return self.ladoSuperior.getConexao()
        
    def ehUmaBuxa(self):
        return self.ladoSuperior.getValor() == self.ladoInferior.getValor() 
        
    def getConexaoInferior(self):
        print("conexao inferior")
        return self.ladoInferior.getConexao()
    
    def meusLadosTemValorIgual(self, ladoDireito:Lado,ladoEsquerdo:Lado):
        return self.ladoSuperior.tenhoOMesmoValor(ladoEsquerdo) or self.ladoInferior.tenhoOMesmoValor(ladoDireito)
            
    def getladoSuperior(self) -> Lado:
        return self.ladoSuperior
    
    def getladoInferior(self) -> Lado:
        return self.ladoInferior
    
    def meDeSeuLadoLivre(self):
        if(self.getConexaoInferior() == None):
            return self.ladoInferior
        if(self.getConexaoSuperior() == None):
            return self.ladoSuperior
            
    def desenhar(self,tela,x,y):
        self.desenharNoConsole()                                         
        self.imagem =  pygame.image.load(os.path.join('Domino\pecasDomino','peca_' + str(self.ladoSuperior.valor) + '.' + str(self.ladoInferior.valor) + '.png')).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem,(50,50))
        pos_centro_imagem = self.imagem.get_rect(topleft=(x,y)).center
        retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem,retangulo.topleft)    
        

    def desenharNoConsole(self):
        print("Oi sou a peça\n" + str(self.ladoSuperior.getValor()) + "\n/" + str(self.ladoInferior.getValor(), "Sou um buxa?", self.ehUmaBuxa()))