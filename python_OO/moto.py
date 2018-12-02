import python_OO.veiculo

class Moto(python_OO.veiculo.Veiculo):
    def __init__(self,  cor,  tipo_combustivel, potencia, marca, passageiro):
        super().__init__(cor,  tipo_combustivel, potencia, marca)
        self.passageiro=passageiro