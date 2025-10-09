soma = 0
contador = 0

num = float(input("Digite um número (negativo para parar): "))

while num >= 0:
    soma = soma + num
    contador = contador + 1
    num = float(input("Digite outro número (negativo para parar): "))

if contador > 0:
    media = soma / contador
    print("Foram inseridos", contador, "números.")
    print("A média é:", media)
else:
    print("Nenhum número válido foi inserido.")
