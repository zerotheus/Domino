from __future__ import annotations
import pygame ,os, random
from Model.Lado import Lado

class Peca:
    imagens = []
    ladoSuperior:Lado 
    ladoInferior:Lado 
    
    def __init__(self, ladoSuperior:Lado, ladoInferior:Lado) -> None:
        self.ladoSuperior = ladoSuperior
        self.ladoInferior = ladoInferior
        ladoSuperior.setPeca(self)
        ladoInferior.setPeca(self)
        pass
    
    def conectar(self,peca:Peca) -> bool:
        self.osLadosConectam(peca)
        
    def osLadosConectam(self,peca) -> bool:
        return self.ladoSuperior.conectaComEstaPeca(peca) or self.ladoInferior.conectaComEstaPeca(peca)
        
    def getConexaoSuperior(self):
        print("conexao superior")
        return self.ladoSuperior.getConexao()
        
    def getConexaoInferior(self):
        print("conexao inferior")
        return self.ladoInferior.getConexao()
            
    def getladoSuperior(self) -> Lado:
        return self.ladoSuperior
    
    def getladoInferior(self) -> Lado:
        return self.ladoInferior
            
    def desenhar(self):
        print("Oi sou a peça\n" + str(self.ladoSuperior.getValor()) + "\n/" + str(self.ladoInferior.getValor()))        
        pass     
