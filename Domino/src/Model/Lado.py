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
    
    def conecta(self, ladoDaOutraPeca:Lado) -> bool:
        if(ladoDaOutraPeca.conexao == None and  self.conexao == None and self.getValor() == ladoDaOutraPeca.getValor()):
            self.setConexao(ladoDaOutraPeca)
            ladoDaOutraPeca.setConexao(self)
            print(self.conexao)
            print(ladoDaOutraPeca.conexao)
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
       
    def setConexao(self,ladoDaOutraPeca:Lado):
        self.conexao = ladoDaOutraPeca
        
    def setPeca(self,peca):
        self.peca = peca