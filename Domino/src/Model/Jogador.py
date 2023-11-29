from Peca import Peca
class Jogador:
    nome: None
    lista_de_Pecas:list[Peca] = []
    vez_de_jogar:bool = None

    def __init__(self,nome):
        self.nome = nome
        pass

    def setPeca(self,peca):
        self.lista_de_Pecas.append(peca)

    def jogarPeca(self,posicao):
        pecaJogada = self.lista_de_Pecas[posicao]
        self.lista_de_Pecas.remove(posicao)
        self.passarVez
        return pecaJogada
    
    def passarVez(self):
        self.vez_de_jogar = False
