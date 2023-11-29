from __future__ import annotations
import pygame ,os, random
from Lado import Lado

class Peca:
    imagens = []
    ladoSuperior:Lado = None
    ladoInferior:Lado = None
    
    def __init__(self, ladoSuperior, ladoInferior) -> None:
        self.ladoSuperior = ladoSuperior
        self.ladoInferior = ladoInferior
        pass
    
    def conectar(self,peca:Peca) -> bool:
        self.osLadosConectam(peca)
        
    def osLadosConectam(self,peca) -> bool:
        return self.ladoSuperior.conectaComEstaPeca(peca) or self.ladoInferior.conectaComEstaPeca(peca)
        
    def getConexaoSuperior(self):
        self.ladoSuperior.getConexao()
        
    def getConexaoInferior(self):
        self.ladoInferior.getConexao()
            
    def getladoSuperior(self) -> Lado:
        return self.ladoSuperior
    
    def getladoInferior(self) -> Lado:
        return self.ladoInferior
            
    def desenhar(self):        
        pass     
    
