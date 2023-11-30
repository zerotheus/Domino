from Model.Peca import Peca
from Model.Lado import Lado

class Jogador:

    def __init__(self,nome):
        self.nome = nome
        self.lista_de_Pecas:list[Peca] = []
        self.vez_de_jogar:bool = None
        pass

    def setPeca(self,peca):
        self.lista_de_Pecas.append(peca)
        self.lista_de_Pecas.sort(key= lambda pecaDaLista: pecaDaLista.getladoSuperior().getValor() + pecaDaLista.getladoInferior().getValor(),reverse=True)

    def setNome(self,nome:str):
        self.nome = nome
        
    def setVezDeJogar(self):
        self.vez_de_jogar = True

    def tenhoBuxa(self):
        for peca in self.lista_de_Pecas:
            if peca.ehUmaBuxa():
                return peca
        return None

    def jogarPeca(self,posicao:int):
        pecaJogada = self.lista_de_Pecas[posicao]
        self.lista_de_Pecas.pop(posicao)
        self.passarVez()
        return pecaJogada
    
    def passarVez(self):
        self.vez_de_jogar = False

    def possoJogar(self,ladoLivreDaDireita:Lado,ladoLivreDaEsquerda:Lado):
        for peca in self.lista_de_Pecas:
            if(peca.meusLadosTemValorIgual(ladoLivreDaEsquerda) or peca.meusLadosTemValorIgual(ladoLivreDaDireita)):
                return True
        return False
    
    def desenharMinhasPecas(self):
        for peca in self.lista_de_Pecas:
            peca.desenhar()
            
    def listarMinhasPecas(self):
        print("Minha quantidade de pecas e", len(self.lista_de_Pecas))
        for peca in self.lista_de_Pecas:
            peca.desenharNoConsole()
            
    def pontosAtuais(self):
        pontos = 0
        for peca in self.lista_de_Pecas:
            pontos += peca.getladoSuperior().getValor() + peca.getladoInferior().getValor()
        return pontos
    
    def executaPrimeiraJogada(self):
        pecaJogada = self.lista_de_Pecas[0]
        self.lista_de_Pecas.pop(0)
        self.passarVez()
        return pecaJogada