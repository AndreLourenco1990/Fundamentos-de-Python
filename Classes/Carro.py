class Motor:
    def __init__(self, CC, CV):
        self.CC = CC
        self.CV = CV
        
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0 
        self.ligado = False  
        print("Carro Criado")

    def ligar_desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True