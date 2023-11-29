from __future__ import annotations

class Lado:
    valor:int = None
    conexao = None
    
    def __init__(self, valor:int) -> None:
        self.valor = valor
        pass
    
    def conecta(self, lado:Lado) -> bool:
        if(lado.conexao == None and self.getValor() == lado.getValor()):
            self.conexao == lado
            lado.conecta()
            return True
        return False
    
    def conectaComEstaPeca(self, peca) -> bool:
        self.conecta(peca.getladoSuperior()) or self.conecta(peca.getladoInferior())
        
    def getValor(self):
       return self.valor
   
    def getConexao(self):
       return self.conexao