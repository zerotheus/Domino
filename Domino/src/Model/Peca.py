from __future__ import annotations
from Lado import Lado

class Peca:
    ladoSuperior:Lado = None
    ladoInferior:Lado = None
    ConexaoSuperior:Peca = None
    ConexaoInferior:Peca = None
    
    
    def __init__(self, ladoSuperior, ladoInferior) -> None:
        self.ladoSuperior = ladoSuperior
        self.ladoInferior = ladoInferior
        pass
    
    def conectar(self,peca:Peca):
        self.ladoSuperior.conectaComEstaPeca(peca)
        self.ladoInferior.conectaComEstaPeca(peca)
        pass
            
    def getladoSuperior(self) -> Lado:
        return self.ladoSuperior
    
    def getladoInferior(self) -> Lado:
        return self.ladoInferior
            
        
         
    
