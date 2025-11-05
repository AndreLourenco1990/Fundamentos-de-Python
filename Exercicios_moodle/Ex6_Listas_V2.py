'''
Nome: André Lourenço
Turma: PI0924
Trabalho: Ex6 - Listas
'''

# EX 1

def ex1_inquerito_criminal():
    print("\n" + "="*50)
    print("EX 1: INQUÉRITO CRIMINAL")
    print("="*50)

    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    respostas_positivas = 0

    for pergunta in perguntas:
        while True:
            resposta = input(f"- {pergunta} (S/N): ").strip().upper()
            if resposta in ('S', 'N'):
                if resposta == 'S':
                    respostas_positivas += 1
                break
            else:
                print("Resposta inválida. Por favor, responda 'S' ou 'N'.")

    if respostas_positivas == 5:
        classificacao = "Assassino"
    elif 3 <= respostas_positivas <= 4:
        classificacao = "Cúmplice"
    elif respostas_positivas == 2:
        classificacao = "Suspeita"
    else:
        classificacao = "Inocente"

    print("\n--- Resultado ---")
    print(f"Classificação: {classificacao}")
    print("-----------------")

# EX 2

def ex2_analise_notas():
    print("\n" + "="*50)
    print("EX 2: ANÁLISE DE NOTAS")
    print("Insira as notas. Termine com -1.")
    print("="*50)

    notas = []
    
    while True:
        try:
            valor = float(input("Nota (-1 para terminar): "))
            if valor == -1:
                break
            notas.append(valor)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            
    if not notas:
        print("Nenhuma nota inserida.")
        return

    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade

    print(f"\nQuantidade de valores lidos: {quantidade}")
    print(f"Valores na ordem de entrada: {' '.join(map(str, notas))}")

    print("Valores na ordem inversa:")
    for nota in reversed(notas):
        print(nota)

    print(f"\nSoma dos valores: {soma:.2f}")
    print(f"Média dos valores: {media:.2f}")

    acima_media = 0
    for nota in notas:
        if nota > media:
            acima_media += 1
    print(f"Quantidade de valores acima da média ({media:.2f}): {acima_media}")

    abaixo_sete = 0
    for nota in notas:
        if nota < 7:
            abaixo_sete += 1
    print(f"Quantidade de valores abaixo de 7: {abaixo_sete}")

    print("\nAnálise de notas concluída.")

# EX 3

def ex3_salarios_vendedores():
    print("\n" + "="*50)
    print("EX 3: SALÁRIOS DE VENDEDORES")
    print("Insira as vendas brutas de cada vendedor. Termine com 0.")
    print("="*50)

    contadores_salarios = [0] * 9 
    SALARIO_BASE = 200
    COMISSAO_PERCENTUAL = 0.09

    vendas_brutas = []
    while True:
        try:
            venda = float(input("Vendas Brutas (0 para terminar): "))
            if venda == 0:
                break
            if venda < 0:
                print("Venda inválida. Insira um valor positivo.")
                continue
            vendas_brutas.append(venda)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    if not vendas_brutas:
        print("Nenhuma venda inserida.")
        return

    for venda in vendas_brutas:
        salario = SALARIO_BASE + (venda * COMISSAO_PERCENTUAL)
    
        indice = int((salario - SALARIO_BASE) / 100)
        
        if indice >= 8:
            indice = 8
        if indice < 0:
            indice = 0
            
        contadores_salarios[indice] += 1
        
    print("\n--- Relatório de Salários ---")
    
    intervalos = [
        "$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
        "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999",
        "$1000 em diante"
    ]
    
    for i in range(len(contadores_salarios)):
        print(f"{intervalos[i]}: {contadores_salarios[i]} vendedores")
        
    print("-----------------------------")

# EX 4

def ex4_salto_em_distancia():
    print("\n" + "="*50)
    print("EX 4: SALTO EM DISTÂNCIA")
    print("Deixe o nome em branco para terminar.")
    print("="*50)

    while True:
        nome_atleta = input("\nNome do Atleta: ").strip()
        
        if not nome_atleta:
            break
            
        saltos = []
        nomes_saltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
        
        for i in range(5):
            while True:
                try:
                    distancia = float(input(f"{nomes_saltos[i]} Salto: "))
                    if distancia < 0:
                        print("A distância deve ser um valor positivo.")
                        continue
                    saltos.append(distancia)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")

        media_saltos = sum(saltos) / len(saltos)
        
        print("\nResultado final:")
        print(f"Atleta: {nome_atleta}")
        saltos_formatados = ' - '.join([f"{s:.1f}" for s in saltos])
        print(f"Saltos: {saltos_formatados}")
        print(f"Média dos saltos: {media_saltos:.1f} m")
        
    print("\nRegisto de saltos concluído.")

if __name__ == "__main__":
    ex1_inquerito_criminal()
    ex2_analise_notas()
    ex3_salarios_vendedores()
    ex4_salto_em_distancia()

