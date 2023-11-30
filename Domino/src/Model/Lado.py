from __future__ import annotations

class Lado:
    valor:int = None
    conexao = None
    peca = None
    
    def __init__(self, valor:int) -> None:
        self.valor = valor
        self.conexao = None
        self.peca = None
        pass
    
    def conecta(self, lado:Lado) -> bool:
        if(lado.conexao == None and  self.conexao == None and self.getValor() == lado.getValor()):
            self.setConexao(lado)
            lado.setConexao(self)
            print(self.conexao)
            print(lado.conexao)
            return True
        return False
    
    def conectaComEstaPeca(self, peca) -> bool:
        return self.conecta(peca.getladoSuperior()) or self.conecta(peca.getladoInferior())
        
    def getValor(self):
       return self.valor
   
    def tenhoOMesmoValor(self,ladoDeOutraPeca:Lado):
        return self.valor == ladoDeOutraPeca.getValor()
   
    def getConexao(self) -> Lado:
       return self.conexao
    
    def getPecaAqualPerteco(self):
        return self.peca
    
    def getDesenheMinhaPeca(self):
        self.peca.desenhar()
   
    def conexaoFazParteDaPeca(self):
       self.conexao.desenhar()
       
    def setConexao(self,lado:Lado):
        self.conexao = lado
        
    def setPeca(self,peca):
        self.peca = peca