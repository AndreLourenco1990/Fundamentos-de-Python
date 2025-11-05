"""
Nome: André Lourenço
Turma: PI 0924
Trabalho: Ex8 - revisões
"""

import sys

#Recolha de dados

def recolher_numeros():
    # Pede a quantidade de números e trata os erros de entrada
    while True:
        try:
            quantidade = int(input("Quantos números deseja inserir? "))
            if quantidade <= 0:
                print("Insira uma quantidade válida (maior que zero).")
                continue
            break
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")
            
    lista_numeros = []
    
    #Pede cada número e trata os erros
    for i in range(quantidade):
        while True:
            try:
                numero = float(input(f"Insira o número {i + 1} de {quantidade}: "))
                lista_numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Insira um número válido.")

    return lista_numeros

#Maior e menor

def achar_maior(lista):
    if not lista:
        return None
    
    #Assume que o primeiro elemento é o maior
    maior = lista[0]
    
    #Compara o maior atual com os restantes elementos
    for numero in lista[1:]:
        if numero > maior:
            maior = numero
            
    return maior

def achar_menor(lista):
    if not lista:
        return None
        
    #Assume que o primeiro elemento é o menor
    menor = lista[0]
    
    #Compara o menor atual com os restantes elementos
    for numero in lista[1:]:
        if numero < menor:
            menor = numero
            
    return menor

#

if __name__ == "__main__":
    
    print("--- Início do Programa ---")
    
    lista_de_numeros = recolher_numeros()
    
    #Verificar se a lista está vazia
    if not lista_de_numeros:
        print("\nNenhum número inserido. Programa encerrado.")
        sys.exit()
        
    print(f"\nLista de números inseridos: {lista_de_numeros}")
    
    #Chamar as funções para encontrar o maior e o menor valor
    valor_maior = achar_maior(lista_de_numeros)
    valor_menor = achar_menor(lista_de_numeros)
    
    #Mostrar o resultado
    print("\n--- Resultado ---")
    print(f"O maior valor inserido é: {valor_maior}")
    print(f"O menor valor inserido é: {valor_menor}")
    print("-----------------")
