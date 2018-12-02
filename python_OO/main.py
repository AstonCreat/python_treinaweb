import python_OO.carro
import python_OO.moto

up = python_OO.carro.Carro("vermelho", "flex", 1.0, "VW", 4)



up.abastecer(50)
up.abastecer(100)
up.abastecer(5)
up.acelerar()

moto_ninja = python_OO.moto.Moto("verde", "gasolina", 600, "ninja", 2)

moto_ninja.ligar()

print(f"moto: {moto_ninja.passageiro}")
print(moto_ninja.is_ligado)