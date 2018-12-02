class Veiculo:
    def __init__(self, cor,  tipo_combustivel, potencia, marca):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.marca = marca
        self.qtd_combustivel=0
        self.is_ligado= False
        self.velocidade = 0

        def __del__(self):
            print("obj foi limpado da memoria")

        def abastecer(self, qtd_combustivel):
            self.qtd_combustivel += qtd_combustivel

        def ligar(self):
            if self.is_ligado:
                print("O veiculo já está ligado")
            else:
                self.is_ligado = True
                print("veiculo foi ligado")

        def desliga(self):
            if self.is_ligado == False:
                print("O veiculo já está desligado")
            else:
                self.is_ligado = False
                print("veiculo foi desligado")

        def acelerar(self, velocidade=10):
            if self.is_ligado:
                self.velocidade += velocidade
                print("velocidade")
                print(f"{velocidade} km/Hr")
            else:
                print("Precisa está ligado para acelerar");
