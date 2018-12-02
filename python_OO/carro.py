import python_OO.veiculo

class Carro(python_OO.veiculo.Veiculo):
    def __init__(self, cor,  tipo_combustivel, potencia, marca, qtd_portas):
        super().__init__(cor,  tipo_combustivel, potencia, marca)
        self.qtd_portas = qtd_portas
