"""
Nome: André Lourenço
Turma: PI0924
Trabalho: Ex7 - ListComp
"""

# EX 1
numeros = [7, -3, 12, 0, -8, 5, -1, 9, -6, 4]

copia = numeros[:]
positivos = [x for x in numeros if x >= 0]
negativos = [x for x in numeros if x < 0]
quadrados = [x**2 for x in numeros]
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

print("Ex 1")
print("Original:", numeros)
print("Cópia:", copia)
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Quadrados:", quadrados)
print("Pares:", pares)
print("Ímpares:", impares)


# EX 2
frase = "Olá mundo! Este é um teste com #Python e #ListComp. Vamos lá?"
palavras = frase.split()

vogais = [l for p in palavras for l in p if l.lower() in 'aeiou']
comprimentos = [len(p.strip(".,!?")) for p in palavras]
minusculas = [p.lower() for p in palavras]
longas = [p.strip(".,!?") for p in palavras if len(p.strip(".,!?")) >= 5]
primeiras = [p[0] for p in palavras if p]
invertidas = [p[::-1] for p in palavras]
tuplos = [(p.strip(".,!?"), len(p.strip(".,!?"))) for p in palavras]
hashtags = [p[1:] for p in palavras if p.startswith('#')]
vogais_unicas = sorted({l.lower() for p in palavras for l in p if l.lower() in 'aeiou'})

print("\nEx 2")
print("Frase:", frase)
print("Vogais:", vogais)
print("Comprimentos:", comprimentos)
print("Minúsculas:", minusculas)
print("Longas (>=5):", longas)
print("Primeiras letras:", primeiras)
print("Invertidas:", invertidas)
print("Tuplos:", tuplos)
print("Hashtags:", hashtags)
print("Vogais únicas:", vogais_unicas)