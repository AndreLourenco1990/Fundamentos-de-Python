"""
Nome: André Lourenço
Turma: PI 0924
Trabalho: Ex 4 - Funções
"""

# =========================
# EX1 – Estrutura Sequencial
# =========================
def ex1_1():
    print("Olá mundo")

def ex1_2():
    n = input("Escreva um número: ")
    print("O número informado foi", n)

def ex1_3():
    a = float(input("Escreva o primeiro número: "))
    b = float(input("Escreva o segundo número: "))
    print("Soma:", a + b)

def ex1_4():
    notas = [float(input(f"Escreva a {i}ª nota: ")) for i in range(1,5)]
    print("Média:", sum(notas)/4)

def ex1_5():
    m = float(input("Escreva o valor em metros: "))
    print("Centímetros:", m*100)

# =========================
# EX2 – Estrutura de Decisão
# =========================
def ex2_1():
    a = float(input("Escreva o 1º número: "))
    b = float(input("Escreva o 2º número: "))
    print("Maior:", a if a>b else b if b>a else "Iguais")

def ex2_2():
    v = float(input("Escreva um valor: "))
    print("Positivo" if v>0 else "Negativo" if v<0 else "Zero")

def ex2_3():
    s = input("Escreva F ou M: ").upper()
    print("F - Feminino" if s=="F" else "M - Masculino" if s=="M" else "Sexo Inválido.")

def ex2_4():
    l = input("Escreva uma letra: ").lower()
    print("Vogal" if l in "aeiou" else "Consoante")

def ex2_5():
    n1 = float(input("Escreva a 1ª nota: "))
    n2 = float(input("Escreva a 2ª nota: "))
    m = (n1+n2)/2
    print("Aprovado com Distinção" if m==10 else "Aprovado" if m>=7 else "Reprovado")

# =========================
# EX3 – Estrutura de Repetição
# =========================
def ex3_1():
    while True:
        n = float(input("Escreva uma nota (0..10): "))
        if 0<=n<=10:
            print("Nota válida:", n); break
        print("Inválida.")

def ex3_2():
    while True:
        u = input("Escreva o utilizador: ")
        s = input("Escreva a senha: ")
        if u==s: print("Erro: senha igual ao utilizador.")
        else: print("Registo aceite."); break

def ex3_3():
    while True:
        nome = input("Nome (>3): ")
        idade = int(input("Idade (0..150): "))
        salario = float(input("Salário (>0): "))
        sexo = input("Sexo (f/m): ").lower()
        ec = input("Estado civil (s/c/v/d): ").lower()
        if len(nome)>3 and 0<=idade<=150 and salario>0 and sexo in "fm" and ec in "scvd":
            print("Dados válidos."); break
        print("Algum dado inválido, tenta de novo.")

def ex3_4():
    a, b, anos = 80000, 200000, 0
    while a < b:
        a = int(a*1.03); b = int(b*1.015); anos += 1
    print(f"Anos: {anos} (A={a}, B={b})")

def ex3_5():
    while True:
        try:
            a = int(input("População A (>0): "))
            b = int(input("População B (>0): "))
            ta = float(input("Taxa A %: "))/100
            tb = float(input("Taxa B %: "))/100
            if a<=0 or b<=0 or ta<0 or tb<0: print("Valores inválidos."); continue
            anos=0
            while a<b and anos<10000:
                a=int(a*(1+ta)); b=int(b*(1+tb)); anos+=1
            print("Impossível em horizonte razoável." if anos>=10000 else f"Anos: {anos} (A={a}, B={b})")
        except ValueError:
            print("Entrada inválida."); continue
        if input("Repetir? (S/N): ").strip().upper()!="S": break