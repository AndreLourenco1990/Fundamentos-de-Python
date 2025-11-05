"""
Nome: André Lourenço
Turma: PI 0924
Trabalho: Ex5 - Listas
"""

#ex1
def ex1():
    print("\n#ex1")
    n = ler_inteiro("n: ")
    for i in range(1, n + 1):
        print(("{}   ".format(i)) * i)


#ex2
def ex2():
    print("\n#ex2")
    n = ler_inteiro("n: ")
    for i in range(1, n + 1):
        linha = [str(x) for x in range(1, i + 1)]
        print("   ".join(linha))


#ex3
def ex3():
    print("\n#ex3")
    v = ler_lista_int(5, "Inteiro")
    print("Vetor lido:", v)


#ex4
def ex4():
    print("\n#ex4")
    v = ler_lista_float(10, "Real")
    print("Ordem inversa:", list(reversed(v)))


#ex5
def ex5():
    print("\n#ex5")
    notas = ler_lista_float(4, "Nota")
    media = sum(notas) / 4
    print("Notas:", notas)
    print("Média:", round(media, 2))


#ex6
def ex6():
    print("\n#ex6")
    consoantes = []
    vogais = set("aeiouáéíóúâêîôûàäëïöüAEIOUÁÉÍÓÚÂÊÎÔÛÀÄËÏÖÜ")
    for i in range(1, 11):
        ch = input(f"Caractere #{i}: ")
        ch = ch[:1]  # apenas o primeiro caractere
        if ch.isalpha() and ch not in vogais:
            consoantes.append(ch)
    print(f"Consoantes lidas: {len(consoantes)}")
    print("Lista de consoantes:", consoantes)


#ex7
def ex7():
    print("\n#ex7")
    nums = ler_lista_int(20, "Inteiro")
    pares = [x for x in nums if x % 2 == 0]
    impares = [x for x in nums if x % 2 != 0]
    print("Todos:", nums)
    print("PAR:", pares)
    print("IMPAR:", impares)


#ex8
def ex8():
    print("\n#ex8")
    medias = []
    for aluno in range(1, 11):
        print(f"- Aluno #{aluno}")
        notas = ler_lista_float(4, "Nota")
        medias.append(sum(notas) / 4)
    aprovados = sum(1 for m in medias if m >= 7.0)
    print("Médias:", [round(m, 2) for m in medias])
    print("N.º de alunos com média >= 7.0:", aprovados)


#ex9
def ex9():
    print("\n#ex9")
    v = ler_lista_int(5, "Inteiro")
    soma = sum(v)
    mult = 1
    for x in v:
        mult *= x
    print("Números:", v)
    print("Soma:", soma)
    print("Multiplicação:", mult)


#ex10
def ex10():
    print("\n#ex10")
    idades = ler_lista_int(5, "Idade")
    alturas = ler_lista_float(5, "Altura (m)")
    print("Idades (inverso):", list(reversed(idades)))
    print("Alturas (inverso):", list(reversed(alturas)))


#ex11
def ex11():
    print("\n#ex11")
    A = ler_lista_int(10, "Inteiro A")
    soma_quadrados = sum(x * x for x in A)
    print("Soma dos quadrados:", soma_quadrados)

#ex12
def ex12():
    print("\n#ex12")
    A = ler_lista_int(10, "A")
    B = ler_lista_int(10, "B")
    C = []
    for a, b in zip(A, B):
        C.extend([a, b])
    print("Intercalado (A,B):", C)

#ex13
def ex13():
    print("\n#ex13")
    A = ler_lista_int(10, "A")
    B = ler_lista_int(10, "B")
    C = ler_lista_int(10, "C")
    D = []
    for a, b, c in zip(A, B, C):
        D.extend([a, b, c])
    print("Intercalado (A,B,C):", D)


#ex14
def ex14():
    print("\n#ex14")
    idades = ler_lista_int(30, "Idade")
    alturas = ler_lista_float(30, "Altura (m)")
    media_altura = sum(alturas) / len(alturas)
    cont = sum(1 for idade, alt in zip(idades, alturas) if idade > 13 and alt < media_altura)
    print("Média de altura:", round(media_altura, 3))
    print("Alunos >13 anos com altura < média:", cont)


#ex15
def ex15():
    print("\n#ex15")
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    temps = ler_lista_float(12, "Temperatura média do mês")
    media_anual = sum(temps) / 12
    print("Média anual:", round(media_anual, 2))
    print("Meses acima da média:")
    for i, t in enumerate(temps):
        if t > media_anual:
            print(f"{i+1} – {meses[i]}: {t}")