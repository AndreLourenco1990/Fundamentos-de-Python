from Pessoa import Pessoa
from Carro import Carro, Motor

c1 = Carro(
    marca="Ford",
    modelo="Fiesta",
    motor=Motor(CC=1000, CV=100)
) 

c2 = Carro(
    marca="Audi",
    modelo="R8",
    motor=Motor(CC=2500, CV=300)
) 

print(f"c1: {c1.marca} {c1.modelo} - {c1.motor.CC}cc, {c1.motor.CV}CV")
print(f"c2: {c2.marca} {c2.modelo} - {c2.motor.CC}cc, {c2.motor.CV}CV")

c1.ligar_desligar()
print(f"{c1.marca} {c1.modelo}: LIGADO")

c1.ligar_desligar()
print(f"{c1.marca} {c1.modelo}: DESLIGADO")