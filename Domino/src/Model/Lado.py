from __future__ import annotations

class Lado:
    valor:int = None
    
    def __init__(self, valor:int) -> None:
        self.valor = valor
        pass
    
    def conecta(self, lado:Lado) -> bool:
        return self.getValor() == lado.getValor()
    
    def conectaComEstaPeca(self, peca) -> bool:
        self.conecta(peca.getladoSuperior()) or self.conecta(peca.getladoInferior())
        
    def getValor(self):
       return self.valor