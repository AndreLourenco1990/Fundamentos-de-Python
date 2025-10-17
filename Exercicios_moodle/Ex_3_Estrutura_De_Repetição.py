"""
Nome: André lourenço
Turma: PI 0924
Trabalho: Ex 3 - Estrutura De Repetição
"""

#Ex1
while True:
    nota = float(input("Escreva uma nota (0 a 10): "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Valor inválido. Tente novamente.")

#Ex2
while True:
    utilizador = input("Escreva o nome de utilizador: ")
    senha = input("Escreva a senha: ")
    if senha == utilizador:
        print("Erro: a senha não pode ser igual ao nome de utilizador.")
    else:
        print("Registo aceite.")
        break

#Ex3
while True:
    nome = input("Escreva o nome (mais de 3 caracteres): ")
    idade = int(input("Escreva a idade (0 a 150): "))
    salario = float(input("Escreva o salário (> 0): "))
    sexo = input("Escreva o sexo (f/m): ").lower()
    estado = input("Escreva o estado civil (s/c/v/d): ").lower()

    if len(nome) <= 3:
        print("Nome inválido.")
        continue
    if not (0 <= idade <= 150):
        print("Idade inválida.")
        continue
    if salario <= 0:
        print("Salário inválido.")
        continue
    if sexo not in ("f", "m"):
        print("Sexo inválido.")
        continue
    if estado not in ("s", "c", "v", "d"):
        print("Estado civil inválido.")
        continue

    print("Dados válidos.")
    break

#Ex4
pop_a = 80000
pop_b = 200000
anos = 0
while pop_a < pop_b:
    pop_a = int(pop_a * 1.03)
    pop_b = int(pop_b * 1.015)
    anos += 1
print(f"Anos necessários: {anos} (A={pop_a}, B={pop_b})")

#Ex5
while True:
    try:
        a = int(input("Escreva a população do país A (inteiro > 0): "))
        b = int(input("Escreva a população do país B (inteiro > 0): "))
        taxa_a = float(input("Escreva a taxa anual de A (%) ex: 3: "))
        taxa_b = float(input("Escreva a taxa anual de B (%) ex: 1.5: "))
        if a <= 0 or b <= 0 or taxa_a < 0 or taxa_b < 0:
            print("Valores inválidos. Tente novamente.")
            continue
        anos = 0
        pa, pb = a, b

        limite = 10000
        while pa < pb and anos < limite:
            pa = int(pa * (1 + taxa_a / 100))
            pb = int(pb * (1 + taxa_b / 100))
            anos += 1

        if anos >= limite:
            print("Com estas taxas, A não ultrapassa B num horizonte razoável.")
        else:
            print(f"Anos necessários: {anos} (A={pa}, B={pb})")
    except ValueError:
        print("Entrada inválida. Use números.")
        continue

    repetir = input("Quer repetir? (S/N): ").strip().upper()
    if repetir != "S":
        break

#Ex6
for i in range(1, 21):
    print(i)
print("---")
for i in range(1, 21):
    print(i, end=" ")
print()  # quebra de linha

#Ex7
maior = None
for i in range(5):
    n = float(input(f"Escreva o {i+1}º número: "))
    if (maior is None) or (n > maior):
        maior = n
print("Maior número:", maior)

#Ex8
soma = 0.0
for i in range(5):
    n = float(input(f"Escreva o {i+1}º número: "))
    soma += n
media = soma / 5
print("Soma:", soma)
print("Média:", media)

#Ex9
for i in range(1, 51):
    if i % 2 == 1:
        print(i)

#Ex10
a = int(input("Escreva o primeiro inteiro: "))
b = int(input("Escreva o segundo inteiro: "))
inicio = min(a, b) + 1
fim = max(a, b)
for i in range(inicio, fim):
    print(i)

#Ex11
a = int(input("Escreva o primeiro inteiro: "))
b = int(input("Escreva o segundo inteiro: "))
inicio = min(a, b) + 1
fim = max(a, b)
soma_intervalo = 0
for i in range(inicio, fim):
    print(i)
    soma_intervalo += i
print("Soma do intervalo:", soma_intervalo)

#Ex12
n = int(input("Escreva um número para ver a tabuada (1 a 10): "))
print(f"Tabuada de {n}:")
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
