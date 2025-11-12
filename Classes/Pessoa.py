class Morada:
    def __init__(self, rua, codigo_postal, porta, apt=None):
        self.rua = rua
        self.codigo_postal = codigo_postal
        self.porta = porta
        self.apt = apt 

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def envelhecer(self, anos=1):
        if self.idade < 25:
            self.altura += 1.5 * anos
        self.idade += anos

def info(pessoa):
    altura_em_metros = pessoa.altura / 100.0

    print("\nInfos:")
    print(f"nome: {pessoa.nome}")
    print(f"idade: {pessoa.idade} anos")
    print(f"altura: {altura_em_metros:.2f} m")

    if pessoa.morada:
        print("Morada:")
        
        apt_str = f" {pessoa.morada.apt}" if pessoa.morada.apt else ""
        print(f"{pessoa.morada.rua} {pessoa.morada.porta}{apt_str}")

        print(f"{pessoa.morada.codigo_postal}")
    else:
        print("Morada: Não definida")