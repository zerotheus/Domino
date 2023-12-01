from Model.Peca import Peca
from Model.Lado import Lado

class Jogador:

    def __init__(self,nome):
        self.nome = nome
        self.lista_de_Pecas:list[Peca] = []
        self.vez_de_jogar:bool = False
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

    def jogadorJogue(self,posicao:int,pecaPraConectar:Peca):
        pecaJogada= self.jogarPeca(posicao)
        return pecaJogada

    def jogarPeca(self,posicao:int):
        pecaJogada = self.lista_de_Pecas[posicao]
        self.lista_de_Pecas.pop(posicao)
        self.passarVez()
        return pecaJogada
    
    def passarVez(self):
        self.vez_de_jogar = False

    def possoJogar(self,ladoLivreDaDireita:Lado,ladoLivreDaEsquerda:Lado):
        print(ladoLivreDaDireita == None,ladoLivreDaEsquerda == None)
        for peca in self.lista_de_Pecas:
            if(peca.meusLadosTemValorIgual(ladoLivreDaEsquerda,ladoLivreDaDireita) or peca.meusLadosTemValorIgual(ladoLivreDaEsquerda,ladoLivreDaDireita)):
                return True
        return False
    
    def possoJogarEssaPeca(self,peca:Peca,pecaLivreDaDireito,ladoEsquerdo):
        return peca.osLadosConectam(pecaLivreDaDireito) or peca.osLadosConectam(ladoEsquerdo)
            
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
    
    def iaJogue(self, ladoEsquerdo:Lado,ladoDireito:Lado, jogo):
        i = 0
        if(self.possoJogar(ladoDireito,ladoEsquerdo)):
            for peca in self.lista_de_Pecas:
                if(peca.meusLadosTemValorIgual(ladoDireito,ladoEsquerdo)):
                    if(peca.conectar(ladoDireito)):
                        jogo.pecaLivreLadoDireito = self.jogarPeca(i) 
                        jogo.adicionaNasJogadas(jogo.pecaLivreLadoDireito)
                        return False
                if(peca.meusLadosTemValorIgual(ladoEsquerdo,ladoEsquerdo)):
                    if(peca.conectar(ladoEsquerdo)):
                        jogo.ladoEsquerdo=self.jogarPeca(i)
                        jogo.adicionaNasJogadas(jogo.ladoEsquerdo)
                        return False
                i+=1
        print("i sai com", i)
        return True