"""
Nome: André Lourenço
Turma: PI 0924
Trabalho: Ex 2 - Estrutura De Decisão
"""

#Ex 1
num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))

if num1 > num2:
    print("O maior número é: ", num1)
elif num2 > num1:
    print("O maior número é: ", num2)
else:
    print("Os números são iguais.")

#Ex 2
valor = float(input("Escreva um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

#Ex 3
sexo = str(input("Escreva a letra do seu sexo (F ou M): "))

if sexo == "F":
    print("O seu sexo é Feminino")
elif sexo == "M":
    print("O seu sexo é Masculino")
else:
    print("Sexo inválido")

#Ex 4
letra = str(input("Escreva uma letra: "))

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

# Ex5
nota1 = float(input("Escreva a 1ª nota: "))
nota2 = float(input("Escreva a 2ª nota: "))
media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção!")
elif media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")

# Ex6
a = float(input("Escreva o 1º número: "))
b = float(input("Escreva o 2º número: "))
c = float(input("Escreva o 3º número: "))

maior = max(a, b, c)
print("O maior número é:", maior)

# Ex7
a = float(input("Escreva o 1º número: "))
b = float(input("Escreva o 2º número: "))
c = float(input("Escreva o 3º número: "))

print("O maior número é:", max(a, b, c))
print("O menor número é:", min(a, b, c))

# Ex8
p1 = float(input("Escreva o preço do 1º produto: "))
p2 = float(input("Escreva o preço do 2º produto: "))
p3 = float(input("Escreva o preço do 3º produto: "))

menor = min(p1, p2, p3)
print("Deves comprar o produto que custa:", menor)

# Ex9
a = float(input("Escreva o 1º número: "))
b = float(input("Escreva o 2º número: "))
c = float(input("Escreva o 3º número: "))

numeros = [a, b, c]
numeros.sort(reverse=True)
print("Números em ordem decrescente:", numeros)

# Ex10
turno = input("Escreva o turno (M - Matutino, V - Vespertino, N - Noturno): ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# Ex11
salario = float(input("Escreva o salário atual (€): "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Salário antes do reajuste: {salario:.2f}€")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: {aumento:.2f}€")
print(f"Novo salário: {novo_salario:.2f}€")
