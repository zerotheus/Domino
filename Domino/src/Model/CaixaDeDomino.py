from Model.Peca import Peca
from Model.Lado import Lado

class CaixaDeDomino:
    
    pecas:list[Peca] = []
    
    def __init__(self) -> None:
        self.geradorDePecas()
        print(self)
        
    
    def geradorDePecas(self):
        if(self.pecas != []):
            return
        for i in range (0, 7):
            for j in range (i,7):
                ladoSuperior = Lado(i)
                ladoInferior = Lado(j)
                self.pecas.append(Peca(ladoSuperior,ladoInferior))
        
    
    def getPecas(self) -> list[Peca]:
        return self.pecas