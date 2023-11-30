from Model.Peca import Peca
from Model.Lado import Lado

class Jogador:
    nome: None
    lista_de_Pecas:list[Peca] = []
    vez_de_jogar:bool = None

    def __init__(self,nome):
        self.nome = nome
        pass

    def setPeca(self,peca):
        self.lista_de_Pecas.append(peca)
        self.lista_de_Pecas.sort(key= lambda pecaDaLista: pecaDaLista.getladoSuperior().getValor() + pecaDaLista.getladoInferior().getValor(),reverse=True)

    def setNome(self,nome:str):
        self.nome = nome

    def tenhoBuxa(self):
        for peca in self.lista_de_Pecas:
            if peca.ehUmaBuxa():
                return peca
        return None

    def jogarPeca(self,posicao):
        pecaJogada = self.lista_de_Pecas[posicao]
        self.lista_de_Pecas.remove(posicao)
        self.passarVez
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