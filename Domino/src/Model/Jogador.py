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

    def jogadorJogue(self,posicao:int):
        return self.jogarPeca(posicao)
        

    def jogarPeca(self,posicao:int):
        pecaJogada = self.lista_de_Pecas[posicao]
        self.lista_de_Pecas.pop(posicao)
        return pecaJogada

    def possoJogar(self,ladoLivreDaDireita:Lado,ladoLivreDaEsquerda:Lado):
        for peca in self.lista_de_Pecas:
            if(peca.meusLadosTemValorIgual(ladoLivreDaEsquerda,ladoLivreDaDireita)):
                return True
        return False
    
    def possoJogarEssaPeca(self,peca:Peca,ladoDireito,ladoEsquerdo):
        return peca.verificaSeConecta(ladoDireito) or peca.verificaSeConecta(ladoEsquerdo)
            
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
        return pecaJogada
    
    def iaJogue(self, ladoEsquerdo:Lado,ladoDireito:Lado, jogo):
        i = 0
        if(self.possoJogar(ladoDireito,ladoEsquerdo)):
            for peca in self.lista_de_Pecas:
                if(peca.meusLadosTemValorIgual(ladoDireito,ladoEsquerdo)):
                    if(peca.conectar(ladoDireito)):
                        pecaJogada = self.jogarPeca(i)
                        jogo.encaixeDireito = pecaJogada.meDeSeuLadoLivre() 
                        #jogo.adicionaNasJogadas(pecaJogada)
                        jogo.pecasNaDir.append(pecaJogada) 
                        return False
                if(peca.meusLadosTemValorIgual(ladoEsquerdo,ladoEsquerdo)):
                    if(peca.conectar(ladoEsquerdo)):
                        pecaJogada = self.jogarPeca(i)
                        jogo.encaixeEsquerdo = pecaJogada.meDeSeuLadoLivre()
                        #jogo.adicionaNasJogadas(pecaJogada)
                        jogo.pecasNaEsq.append(pecaJogada) 
                        return False
                i+=1
        print("i sai com", i)
        return True