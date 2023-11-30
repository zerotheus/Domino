from Model.CaixaDeDomino import CaixaDeDomino
from Jogo import Jogo
from Model.Jogador import Jogador

def test():
    caixa:CaixaDeDomino = CaixaDeDomino()
    pecas = caixa.getPecas()
    for peca in pecas:
        peca.desenharNoConsole()
    
    print("Pecas geradas", len(pecas))
        
    print("conectou?", pecas[0].conectar(pecas[1]))
    
    print("0/0",pecas[0].getConexaoSuperior())
    print("0/0",pecas[0].getConexaoInferior())
    print("0/1",pecas[1].getConexaoSuperior())
    print("0/1",pecas[1].getConexaoInferior())
    
    print(pecas[0].getladoSuperior().getValor())
    print(pecas[0].getladoInferior().getValor())
    print(pecas[1].getladoSuperior().getValor())
    print(pecas[1].getladoInferior().getValor())
    
    print(pecas[0].getladoSuperior())
    print(pecas[0].getladoInferior())
    print(pecas[1].getladoSuperior())
    print(pecas[1].getladoInferior())
    #peca 0/1 == a conexao superior da peça 0/0?    
    print(pecas[1] == pecas[0].getConexaoSuperior().getPecaAqualPerteco())
    
    print(pecas[0].conectar(pecas[2]))
    print("0/0",pecas[0].getConexaoSuperior())
    print("0/0",pecas[0].getConexaoInferior())
    
    #peca 0/2 == a conexao superior da peça 0/0?    
    print(pecas[2] == pecas[0].getConexaoSuperior().getPecaAqualPerteco())
    #peca 0/2 == a conexao inferior da peça 0/0?    
    print(pecas[2] == pecas[0].getConexaoInferior().getPecaAqualPerteco())
    #peca 0/3 conecta?    
    print("peca 03 conecta?", pecas[0].conectar(pecas[3]))

    jogo:Jogo = Jogo()
    jogador:Jogador = jogo.getJogador()
    jogador.listarMinhasPecas()
    jogo.quantidadeDePecas()
    jogo.embaralhar()
    jogo.quantidadeDePecas()
    jogador.listarMinhasPecas()
    print(jogador.pontosAtuais())
    print(jogador.tenhoBuxa())
    jogo.defineOrdemDeJogada()
    
test()