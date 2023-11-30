from __future__ import annotations
import pygame ,os, random
from Model.Lado import Lado

class Peca:
    imagens = None
    ladoSuperior:Lado 
    ladoInferior:Lado 
    posicaoX:float = 200
    posicaoY:float = 500
 
    def __init__(self, ladoSuperior:Lado, ladoInferior:Lado) -> None:
        self.ladoSuperior = ladoSuperior
        self.ladoInferior = ladoInferior
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
            
    def desenhar(self,tela):
        print("Oi sou a peça\n" + str(self.ladoSuperior.getValor()) + "\n/" + str(self.ladoInferior.getValor()))
        self.imagem =  pygame.image.load(os.path.join('Domino\pecasDomino','peca_0.0.png')).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem,(50,50))
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.posicaoX,self.posicaoY)).center
        retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        
        tela.blit(self.imagem,retangulo.topleft)    
